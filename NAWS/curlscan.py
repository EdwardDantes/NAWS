import logging.config
import logging
from pycurl import curl

logging.config.fileConfig("logger.conf")
logger = logging.getLogger(__name__)


class CurlSession(Object):
    """
        emulate and automate these commands
        curl -Is https://www.twitter.com -L
        curl  smtp://mail.steelnetwork.com:25 -v
        curl  smtp://mail.steelnetwork.com:465 -v
        curl  smtp://mail.steelnetwork.com:587 -v
    """

