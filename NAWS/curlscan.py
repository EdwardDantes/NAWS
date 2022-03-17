import logging.config
import logging
import pycurl
import napalm
from sys import argv
from sys import exit

logging.config.fileConfig("logger.conf")
logger = logging.getLogger(__name__)


class GetTarget(Object):

    def getArgs(argv)
      