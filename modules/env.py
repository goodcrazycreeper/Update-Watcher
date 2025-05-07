import os
import sys
from dotenv import load_dotenv
def loadEnvironmentVar(select):
    returnVal = None
    load_dotenv()
    match select:
        case "KEY":             
            returnVal = {"X-API-KEY": os.getenv("X-API-KEY")}
        case "TOKEN":
            returnVal = os.getenv("TOKEN")
    if returnVal == None:
        print(f"\33[33m{__name__}:WARN: NO .ENV FOUND! CREATE .ENV IN MAIN DIRECTORY\33[0m")
        sys.exit() # If returnVal returns None script will exit
    return returnVal