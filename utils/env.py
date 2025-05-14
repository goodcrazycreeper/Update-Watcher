import os
import sys
from dotenv import load_dotenv


def loadEnvironmentVar(select):
    ReturnVal = None
    load_dotenv()
    match select:
        case "KEY":
            ReturnVal = {"X-API-KEY": os.getenv("X-API-KEY")}
        case "TOKEN":
            ReturnVal = os.getenv("TOKEN")
    if ReturnVal == None:
        print(
            f"\33[33m{__name__}:WARN: NO .ENV FOUND! CREATE .ENV IN MAIN DIRECTORY\33[0m"
        )
        sys.exit()  # If ReturnVal returns None script will exit
    return ReturnVal
