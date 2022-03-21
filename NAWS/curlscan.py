"""
curlscan utilizes the pycurl library to open an http or smtp session and provides
header values, cookie values, contents of html, css, json, xml, or javascript located
within the url specified.
These values are reported and recorded in such a way that the wfuzz engine can be automated
to attack the vectors discovered. 
Any successful status codes from wfuzz can then be rescaned with curl to search for vulnerable 
responses within the html body. 
"""



import logging.config
import logging
from pycurl import curl

"""
Use Logging within curlscan. In logging library the class Handler has subclasses, SMTPHandler and HTTPHandler.
"""

logging.basicConfig(filename='~/var/logs/NAWS.log', filemode='w')
logger = logging.getLogger(__name__)

http_log_handler = logging.HTTPHandler() #debug
smtp_log_handler = logging.SMTPHandler() #debug
mem_log_handler = logging.MemoryHandler() #critical
file_handler


class CurlSession(Object):

    def __init__(self)

    def startCurlSession(self, url)
    """
        emulate and automate these commands
        curl -Is https://www.twitter.com -L
        curl  smtp://mail.google.com:25 -v
        curl  smtp://mail.google.com:465 -v
        curl  smtp://mail.google.com:587 -v 
    """
    try:
        
        session = setopt(URL, f'{url}')
    except Exception as e:
        logging.error("Exception occurred", exc_info=True)



    #open the url session
    #save and store cookies if required.

    def getCurlHeaders()
    def getCurlCookies()
    """
    Returns the headers of url response in a dictionary form. 
    """
    def 


