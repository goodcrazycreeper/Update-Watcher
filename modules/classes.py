""" 
This module is responsible for getting the dates of when a game was updated and its subplaces.
"""
import modules.reqmethods as req
import modules.env as env
X_API_KEY = env.loadEnvironmentVar("KEY")

class Universe(): # A class named universe, which a group of places/games with one of the places being the rootPlace(game page)
    def __init__(self, universeName=None,rootPlaceId=None, universeId=None,  path=None):
        self.universeName = universeName
        self.universeId = universeId
        self.rootPlaceId = rootPlaceId
        self.path = path

class Subplace(Universe): # A classed named subplace, which belongs to a universe which defines a place 
    def __init__(self, universeId,placeId, rootPlaceId, path, updateTime, displayName:str, isRootPlace: bool):
        super().__init__(universeId, rootPlaceId, path)
        self.isRootPlace = isRootPlace # Bool
        self.updateTime = updateTime
        self.displayName = displayName

        def fillInfo():
            r =  req.getMethod(url=f"https://apis.roblox.com/cloud/v2/universes/{universeId}/places/{placeId}",headers=X_API_KEY)["data"]
            self.updateTime = r["updateTime"]