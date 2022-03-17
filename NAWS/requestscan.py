import logging.config
import logging
from pycurl import curl

logging.config.fileConfig("logger.conf")
logger = logging.getLogger(__name__)


class RequestsSession(Object):