import logging

DEBUG = True
APP_NAME = 'EDGAR'
EDGAR_HOST = '0.0.0.0'
EDGAR_PORT = 80
API_VERSION = (0, 0, 1)

LOG_LEVEL = logging.DEBUG
LOG_FMT = "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s"
LOG_FORMATTER = logging.Formatter(LOG_FMT)
