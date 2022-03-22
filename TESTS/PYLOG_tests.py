"""
Unittest based testing with additional logging and conditionals for further depth to troubleshooting from results.
"""

import unittest
import logging.config
import logging
import json
#import CurlSession from culscan #fix

logging.basicConfig(filename='~/var/logs/NAWSunittest.log', filemode='a')
logger = logging.getLogger(__name__)

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

    
    def test_xml_output(self):
        """
        Test the conversion of output to XML, with the same header value as in test_status_response.
        """

    def test_output_file(self):
        try:
            with open(f"{self.filename}"):

if __name__ == "__main__":
    classtocall()



