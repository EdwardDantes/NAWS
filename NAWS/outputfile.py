import json
import xmltodict
import csv
import logging


class formatOutput(Object):
    
    def __init__(self, info, mode, filename):
        """
        info
        status
        """

    def xmlOutput(self, info):
        """
        Make the output file xml.
        """

    def csvOutput(self, info):
        """ 
        Make the output file csv.
        """   
        with open(f'{filename}', mode=f'{mode}') as infile:
            reader = csv.reader(infile)
            with open(f'{filename}', mode=f'{mode}') as outfile:
                writer = csv.writer(outfile)
                mydict = {rows[0]:rows[1] for rows in reader}
            print(mydict)

    def jsonOutput(self, info)
        """
        Make the output file json.
        """

