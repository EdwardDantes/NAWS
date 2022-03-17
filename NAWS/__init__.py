from introtext import welcomeflag
from argread import argumentReader
from curlscan import CurlSession #website url status and headers
from requestscan import RequestSession
from nmapscan import NmapResults
from napalmscan import NapalmSession
from fuzzed import fuzzOff #Run each form of injection type in each header and return http status codes

if __name__== "__main__":
    """
    inputs: url, mode, outputfile, typeofoutput, type of scan (info, offensive, web, email)
    """



