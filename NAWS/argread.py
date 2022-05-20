from sys import argv
import logging.config
import logging  #Debug, info, warning, error, critical
import json


logging.config.fileConfig("NAWSlogger.conf")
logger = logging.getLogger(__name__)

class argumentReader():
    """
    Read Kwargs and use cases to get results.
    """
    def __init__(self):
        """
        Nothing to see here.
        """
        
    def Decisions(self):
        logger.info("Class argument Reader -> function Decisions")
        NewArgs = argv
        i = 0
        #Arguement_Dict = {0: "Null"}
        if (len(NewArgs)) >= 6:
            logger.critical("ERROR: Too many arguements.")
            print("Too many arguements on the command line. Type NAWS -h for help menu.")
        elif (len(NewArgs) == 1):
            logger.critical("ERROR: Too few arguements.")
            print("NAWS requires multiple arguements. Type python3 Hoggin.py -h for help menu.")
        elif (len(NewArgs) >= 2 or len(NewArgs) <= 5):
            print("Processing.")

        Arguement_Dict  = {i: NewArgs[i] for i in range(0, len(NewArgs), 1)}
        Specific_Dict = {"url": "NULL", "mode": "NULL", "outputfilename": "NULL"}
        logger.info(f"Command Line Arguements have been recieved. {NewArgs}")  
 
        for values in Arguement_Dict:  
            if (Arguement_Dict[values] == '-h'):
                print("Welcome to NAWS \"Not Another Web Scanner\". This is a simple script to automate a series of HTTP Analyis tools against Web and Email servers. \n")
                print("Provide the url and output file type and name to run the automated scan.\n")
                print("NAWS -u <url> -p <port(s) individual 25,443 or range 25:443> -m <mode> -t <file type> -o <file name>   \n")
                print("examples:\n")
                print("python3 naws.py -u url")
                print("python3 naws.py -u myUsername -o filename.rules")
                print("python3 naws.py -f /home/username/Desktop/github/wordlist/commands.txt -o outputresults.txt \n")
                exit()

            elif(Arguement_Dict[values] == '-u'):
                Specific_Dict["url"] = Arguement_Dict[values+1] 

            elif(Arguement_Dict[values] == '-m'):
                Specific_Dict["mode"] = Arguement_Dict[values+1] 
                
            elif(Arguement_Dict[values] == '-p'):
                Specific_Dict["port(s)"] = Arguement_Dict[values+1]
                #split range of ports with a coma as individual or colon as a range.  

            elif(Arguement_Dict[values] == '-t'):
                Specific_Dict["file_type"] = Arguement_Dict[values+1]

            elif(Arguement_Dict[values] == '-o'):
                Specific_Dict["outputfilename"] = Arguement_Dict[values+1]

                try:
                    logger.info("Outpute file has been specified.")
                    with open(f'{Specific_Dict["outputfilename"]}') as outfile:
                        json.dump("Begin Scan", outfile, indent = 2) 
                        

                except:
                    logger.critical("Output file specification failed.")


        logger.info("Returning standard dict from Decisions <- argumentReader ")
        return Specific_Dict


#Output in XML, JSON, CSV, or TXT