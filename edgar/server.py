import os

from waitress import serve

from app import create_app

grid = os.environ.get('GRID', 'dev')
app = create_app(env=grid)

if __name__ == '__main__':
    serve(app, host=app.config['EDGAR_HOST'], port=app.config['EDGAR_PORT'])
