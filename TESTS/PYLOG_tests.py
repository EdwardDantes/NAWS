"""
Unittest based testing with additional logging and conditionals for further depth to troubleshooting from results.
"""

import unittest
import logging.config
import logging
import json
import xmltodict
import os 
import platform 
#import CurlSession from culscan #fix

system = platform.system()
user = os.getlogin() 
FORMAT = '%(asctime)s %(system)s %(user)-8s %(levelno)s %(message)s'
logging.basicConfig(filename='~/var/logs/NAWSunittest.log', filemode='a', format=FORMAT)
logger = logging.getLogger(__name__)
#LogLevel: value {'Critial': '50', 'Error':'40', 'Warning': '30', 'Info':'20', 'Debug':'10', 'Notset': '0'}

class TestCurlResponses(unittest.TestCase):

    def __init__(self):
        self.test_url = "www.google.com"
        self.filename = ""

    def test_status_response(self):
        """
        Test Http Response Header in Curl Response.
        """
        try:
            self.csession = CurlSession()
            self.cresponse = self.csession.startCurlSession(self.test_url)
            self.json_response = json.loads(self.cresponse)
            expected_output = {'someheader': 'its value'}
            expected_header_value = '201'
        except Exception as e:
            logging.error(f"Unittest function test_json_output failed because of {e} and additional information:", exc_info=True)
        try:
            self.ctest.assertEquals(self.json_response, (json.dumps(expected_output)),expected_header_value)
        except:
            logging.error(f"Unittest function test_json_output status response failed because {e} and additional information:", exc_info=True)
    
    def test_xml_output(self, xml_data):
        """
        Test the conversion of output to XML, with the same header value as in test_status_response.
        """
        if xml_data:
            xml_test = xml_data.read()
            xml_dict = xmltodict.parse(xml_test)
        else:

    def test_output_file(self):
        """
        Test existance of output file. 
        """
        try:
            with open(f"{self.filename}") as file:
                if file:
                    print("File output test: SUCCESS")
                    logging.info("File output tested Successfully.")
                else:
                    print("File does not exist or cannot be opened.")
                    logging.error("File output test failed.")
        except Exception as e:
             logging.error(f"Unittest function output file failed because of {e} and additional information:", exc_info=True)

    if __name__ == "__main__":
        #call logger and set log level
        unittest.main()




