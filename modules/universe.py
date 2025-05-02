# Universe.py responsible for retrieving universe data such as number of subplaces.
import requests
import time
from functools import wraps

def check_key_exists(d, key): 
    return key in d # Check if the 'address' key exists in the dictionary

def getMethod(url,*args,**kwargs): # Return dict
    try:
        response = requests.get(url,*args,**kwargs) # Translate placeid into universeid
    except:
         return "An error occured " + response.status_code
    return {"data": response.json(), "status": response.status_code}

def getUniverseData(placeId):
    UniverseID = getMethod(f'https://apis.roblox.com/universes/v1/places/{placeId}/universe')["data"]["universeId"] # TypeError: 'NoneType' object is not callable
    UniverseData = getMethod(f'https://develop.roblox.com/v2/universes/{UniverseID}/places')
    return UniverseData

class Universe(): # A class named universe, which a group of places/games with one of the places being the rootPlace(game page)
    def __init__(self, rootPlaceId, universeId=None,  path=None): # Class constructor
        self.universeId = universeId
        self.rootPlaceId = rootPlaceId
        self.path = path
    def initilizeUniverseData(placeId):
          data = getUniverseData(placeId)
          Universe.universeId = data

# https://develop.roblox.com/v2/universes/7296012067/places

# BadRequest = Universe(72960120933333399999999999999967)

