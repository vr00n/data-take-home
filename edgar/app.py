import logging
import sys

from flask import Flask

from views import views


def create_app(env=None):
    """An application factory, as explained here:
        http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    configure_app(app, env=env)
    configure_logger(app)

    @app.after_request
    def populate_headers(resp):
        version = '.'.join(map(str, app.config['API_VERSION']))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Allow-Methods'] = 'OPTIONS, GET'
        resp.headers['Server'] = '%s/%s' % (app.config['APP_NAME'], version)
        resp.headers['X-Api-Version'] = version
        return resp

    app.register_blueprint(views)

    return app


def configure_app(app, env=None, **kwargs):
    app.config.from_object('.'.join(['config', env]))
    return app


def configure_logger(app, **kwargs):
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(app.config['LOG_LEVEL'])
    handler.setFormatter(app.config['LOG_FORMATTER'])
    app.logger.addHandler(handler)
    return app
