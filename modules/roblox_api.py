""" 
This module is responsible for getting the dates of when a game was updated and its subplaces.
"""
import requests

def getUniverseData(placeId):
    response = requests.get(f'https://apis.roblox.com/universes/v1/places/{placeId}/universe') # Get universe ID if none is supplied
    response = requests.get(f"https://develop.roblox.com/v2/universes/{response.json()["universeId"]}/places")
    jSonData = response.json()
    
    if response.status_code == 200: # Debugging purposes
        try:
            print(jSonData["errors"])
        except:
            print(jSonData)
        finally:
            try:
                print(jSonData["data"])
            except:
                print(jSonData)

class Universe: # A class named universe, which a group of places/games with one of the places being the rootPlace(game page)
    def __init__(self, universeId, rootPlaceId, gameLink): # Class constructor
        self.universeId = universeId
        self.rootPlaceId = rootPlaceId
        self.gameLink = gameLink

class Subplace(Universe): # A classed named subplace, which belongs to a universe which defines a place 
    def __init__(self, universeId, rootPlaceId, gameLink, updateStamp, name:str, isRootPlace: bool):
        super().__init__(universeId, rootPlaceId, gameLink)
        self.name = name
        self.isRootPlace = isRootPlace
        self.updateStamp = updateStamp

# FREEDOMWAR = Subplace(4096039463,11534222714,"https://roblox.com/games/11534222714","2025-04-28T02:06:43.57767Z","Attack on Titan: Freedom War",True)
# print(FREEDOMWAR.__dict__)