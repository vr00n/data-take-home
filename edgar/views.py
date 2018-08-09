import logging
from datetime import datetime

from flask import abort, Blueprint, render_template, request, redirect
from flask.ext.paginate import Pagination

from faker import Factory

logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)
views = Blueprint('view', __name__)
fake = Factory.create()


def log_request(req, status=200):
    template = '{ip} - - "{method} {uri} {protocol}" {time} - - {status}'
    context = {
        'ip': req.environ.get("REMOTE_ADDR"),
        'time': datetime.utcnow().isoformat(),
        'method': req.method,
        'uri': req.path,
        'protocol': req.scheme,
        'status': status
    }
    logger.info(template.format(**context))


def generate_companies():
    for _ in range(100):
        COMPANIES.append({
            'name': fake.company(),
            'street_address': fake.street_address(),
            'street_address_2': fake.secondary_address(),
            'city': fake.city(),
            'state': fake.state(),
            'zipcode': fake.zipcode(),
            'phone_number': fake.phone_number(),
            'website': fake.domain_name(),
            'description': fake.bs()
        })

COMPANIES = []
generate_companies()


def fetch_ten(company_names, page, per_page):
    ceiling = page * per_page
    return company_names[ceiling-10:ceiling]


@views.route('/')
def index():
    return redirect('/companies/')


@views.route('/companies/')
def company_listings():
    page = int(request.args.get('page', 1))
    per_page = request.args.get('per_page', 10)

    total_companies = len(COMPANIES)
    company_names = [c['name'] for c in COMPANIES]
    page_company_names = fetch_ten(company_names, page, per_page)

    if not company_names and page != 1:
        abort(404)

    pagination = Pagination(
        css_framework='bootstrap3',
        link_size='sm',
        page=page,
        per_page=per_page,
        total=total_companies,
        record_name='companies'
    )

    log_request(request)

    return render_template(
        'company_listings.html',
        company_names=page_company_names,
        page=page,
        per_page=per_page,
        pagination=pagination
    )


@views.route('/companies/<string:company_name>')
def company_listing(company_name):
    for company in COMPANIES:
        if company['name'] == company_name:
            log_request(request)
            return render_template(
                'company.html',
                company=company
            )
