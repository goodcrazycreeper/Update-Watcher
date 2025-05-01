# Universe.py responsible for retrieving universe data such as number of subplaces.
import requests

def check_key_exists(d, key): 
    # Check if the 'address' key exists in the dictionary
    return key in d
def getProtector(func): # Function for get Method just incase 200 isnt returned
     def wrapper(*args):
            try:
                func(*args)
                return wrapper
            finally:
                                
    
@getProtector
def getMethod(url,*args):
        try: 
            response = requests.get(f'https://apis.roblox.com/universes/v1/places/{placeId}/universe') # Get universe ID if none is supplied
            if response.status_code == 400:  
                    return response.json()["errors"][0] # Returns the error table of 400
                
    response = requests.get(f"https://develop.roblox.com/v2/universes/{response.json()["universeId"]}/places")
    jSonData = response.json()
           
def getUniverseData(placeId):

    
    if response.status_code == 200: # Debugging purposes
            print(jSonData[""])
    elif response.status_code == 400:
            print(jSonData["errors"][0]["code"])
    else:
            pass
class Universe(): # A class named universe, which a group of places/games with one of the places being the rootPlace(game page)
    def __init__(self, rootPlaceId, universeId=None,  path=None): # Class constructor
        self.universeId = universeId
        self.rootPlaceId = rootPlaceId
        self.path = path
    def initilizeUniverseData(placeId):
          getUniverseData(placeId)
          Universe.universeId = 

# https://develop.roblox.com/v2/universes/7296012067/places

BadRequest = Universe(72960120933333399999999999999967)