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
from pycurl import Curl
from io import BytesIO
import certifi
import json

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

    def __init__(self):
        """
        All curl base operations will start from this class. 
        """
        self.c = Curl() 
        self.buffer = BytesIO()
        self.success = 'NULL'
        self.response = 'NULL'


    def startCurlSession(self, url, data_format):
        """
            Starts a curl session and returns the entire server response. 
            emulate and automate these commands
            curl -Is https://www.twitter.com -L
            curl  smtp://mail.google.com:25 -v
            curl  smtp://mail.google.com:465 -v
            curl  smtp://mail.google.com:587 -v  
        """
        self.url = url
        self.data_format = "txt"
        try:
            self.c.setopt(self.c.URL, f'{url}')
            self.c.setopt(self.c.WRITEDATA, self.buffer)
            self.c.setopt(self.c.CAINFO, certifi.where())
            self.c.perform()
            self.success = "TRUE"
        except Exception as e:
            logging.error("Exception occurred", exc_info=True)
        finally:
            self.c.close()

        #Setup buffer for the curl session.
        if self.success == "TRUE":
            try:
                self.response = self.buffer.getvalue()
                self.response_dict = json.loads(self.response)
            except Exception as e:
                logging.error("Failed to load curl response to json format.", exc_info=True)
        else:
            logging.error("No data to load into json format.")


        

    #open the url session
    #save and store cookies if required.

    def getCurlHeaders():
        """
        Returns a dictionary of Headers used by the target URL.
        """

    def getCurlCookies():
        """
        Returns the headers of url response in a dictionary form. 
        """
    
    def findPHPinCurlSession():
        """
        use regex to find embedded php components of server response or links to php files.
        """

    def findJavaScriptinCurlSession():
        """
        use regex to find embedded script tags or links to .js files. 
        """
    
    def findFormParametersinCurlSession():
        """
        use regex to find "=" in lines and extract parameter names, places, and values.
        """
    
    def changeCurlHeaders():
        """
        Retarget website with new headers.  This function may be more useful under Wfuzz components.
        """


