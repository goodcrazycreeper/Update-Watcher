# Universe.py responsible for retrieving universe data such as number of subplaces.
import requests
from functools import wraps

def check_key_exists(d, key): 
    return key in d # Check if the 'address' key exists in the dictionary

def getProtector(func): # Function for get Method just incase 200 isnt returned
     # @wraps(func)
     def wrapper(*args, **kwargs):
            try:
                result = func(*args,**kwargs)
                # if isinstance(result, tuple) and len(result) == 2: # if the return value of func is a tupel and the length is 2 
                data, status = result
                if status == 200:
                    print("Success:", status)
                elif status == 400 and "errors" in data:
                    return data["errors"][0]
                else:
                    print(f"Unhandled status code: {status}")
                return result
                # else:
                #     print("Unexpected return format from function.")
                #     return result
            except Exception as e:
                    print("An exception occurred:", e)
                    return {"error": str(e)}, 500
            return wrapper
@getProtector
def getMethod(url,*args,**kwargs): # Return dict
    response = requests.get(url,*args,**kwargs) # Translate placeid into universeid
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