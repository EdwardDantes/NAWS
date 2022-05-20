from NAWS.introtext import welcomeflag
from NAWS.argread import argumentReader
from NAWS.curlscan import CurlSession #website url status and headers
from NAWS.requestscan import RequestSession
from NAWS.nmapscan import NmapResults
from NAWS.napalmscan import NapalmSession
from NAWS.fuzzed import fuzzOff #Run each form of injection type in each header and return http status codes



if __name__== "__main__":
    """
    inputs: url, mode, outputfile, typeofoutput, type of scan (info, offensive, web, email)
    """

#Startup and intro.
intro = welcomeflag()
instance = argumentReader()




