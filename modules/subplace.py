""" 
This module is responsible for getting the dates of when a game was updated and its subplaces.
"""
import requests
import os
import sys
import universe
from os import getenv
from dotenv import load_dotenv
try:
    load_dotenv()
    X_API_KEY = os.getenv("X-API-KEY")
finally:
    if X_API_KEY == None:
        print("\33[33mWARN: NO .ENV FOUND! CREATE .ENV IN MAIN DIRECTORY\33[0m")
        sys.exit() # If X_API_KEY returns None script will exit

class Subplace(universe.Universe): # A classed named subplace, which belongs to a universe which defines a place 
    def __init__(self, universeId, rootPlaceId, path, updateTime, displayName:str, isRootPlace: bool):
        super().__init__(universeId, rootPlaceId, path)
        self.displayName = displayName
        self.isRootPlace = isRootPlace # Bool
        self.updateTime = updateTime

        def fillInfo():
            r =  requests.get(url="https://apis.roblox.com/cloud/v2/universes/7296012067/places/83139067970039",headers=X_API_KEY)

