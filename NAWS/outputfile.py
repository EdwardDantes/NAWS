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

    def xmlOutput(self, filename, write_data, verbose):
        """
        Make the output file xml.
        """
        with open(f"{filename}") as infile:
            xml_data =

    def csvOutput(self, filename, mode, write_data, verbose):
        """ 
        Make the output file csv.
        """   
        try:
            logger.info(f"Attempting to open the CSV output file: {filename}")
            with open(f'{filename}', mode=f'{mode}') as infile:
                reader = csv.reader(infile)
                logger.info(f"Attempting to write to already existing CSV file: {filename} ")
                with open(f'{filename}', mode=f'{mode}') as outfile:
                    writer = csv.writer(outfile)
                    mydict = {rows[0]:rows[1] for rows in reader}
        except:
            logger.critical(f"No file found attempting to write new CSV file: {filename} ")
            with open(f'{filename}', mode=f'{mode}') as outfile:
                writer = csv.writer(outfile)
                mydict = {rows[0]:rows[1] for rows in reader}
        finally:
            if verbose == 'true':
                print(mydict)

    def jsonOutput(self, filename, mode, write_data, verbose)
        """
        Make the output file json.
        """
        try:
            logger.info(f"Attempting to open or create the Json Output File. {filename}")
            with open(f"{filename}", mode=f'{mode}') as infile:

                json.dump(json_dict, infile, indent = 4)

