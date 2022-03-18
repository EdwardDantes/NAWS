import logging.config
import logging
import requests

logging.config.fileConfig("logger.conf")
logger = logging.getLogger(__name__)


class RequestsSession(Object):