from sys import argv
import logging.config
import logging


logging.config.fileConfig("logger.conf")
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
            print("Too many arguements on the command line. Type python3 Hoggin.py -h for help menu.")
        elif (len(NewArgs) == 1):
            logger.critical("ERROR: Too few arguements.")
            print("Hoggin.py requires multiple arguements. Type python3 Hoggin.py -h for help menu.")
        elif (len(NewArgs) >= 2 or len(NewArgs) <= 5):
            print("Processing.")

        Arguement_Dict  = {i: NewArgs[i] for i in range(0, len(NewArgs), 1)}
        Specific_Dict = {"url": "NULL", "": "NULL", "outputname": "NULL"}
        logger.info(f"Command Line Arguements have been recieved. {NewArgs}")  
 
        for values in Arguement_Dict:  
            if (Arguement_Dict[values] == '-h'):
                print("Welcome to NAWS \"Not Another Web Scanner\". This is a simple script to automate a series of HTTP Analyis tools against Web and Email servers. \n")
                print("Provide either you username or a file with a list of words/commands/otherwise you want the snort rule to find.\n")
                print("python3 Hoggins.py <options> <arguments>\n")
                print("examples:\n")
                print("python3 naws.py -u url")
                print("python3 naws.py -u myUsername -o filename.rules")
                print("python3 naws.py -f /home/username/Desktop/github/wordlist/commands.txt -o outputresults.txt \n")
                exit()
            elif(Arguement_Dict[values] == '-u'):
                Specific_Dict["username"] = Arguement_Dict[values+1] 

            elif(Arguement_Dict[values] == '-f'):
                Specific_Dict["filename"] = Arguement_Dict[values+1] 
                
            elif(Arguement_Dict[values] == '-o'):
                Specific_Dict["outputname"] = Arguement_Dict[values+1] 

        logger.info("Returning standard dict from Decisions <- argumentReader ")
        return Specific_Dict


#Output in XML, JSON, CSV, or TXT