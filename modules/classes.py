""" 
This module is responsible for getting the dates of when a subplace in a universe was updated.
"""
import modules.reqmethods as req
import modules.env as env
X_API_KEY = env.loadEnvironmentVar("KEY")

class Universe(): # A class named universe, which a group of places/games with one of the places being the rootPlace(game page)
    def __init__(Self, PlaceId):
        Self._PlaceId = PlaceId
        Self._UniverseId = None # req.GetUniverseId(PlaceId)
        Self.__UniverseName = None
        Self.__RootPlaceId = None
        Self._Path = None
    def _DefineUniverse(PlaceId):
        req.GetUniverseData(PlaceId)
        pass
    


class Subplace(Universe): # A classed named subplace, which belongs to a universe which defines a place 
    def __init__(Self, PlaceId):
        super().__init__(PlaceId)
        Self.IsRootPlace: bool = False # Bool
        Self._UpdateTime: str = None
        Self._DisplayName: str = None

        

    def FillInfo(Self):
        url = f"https://apis.roblox.com/cloud/v2/universes/{UniverseId}/places/{PlaceId}"
        r =  req.GetMethod(url,headers=X_API_KEY)["data"]
        Self._updateTime = r["updateTime"]
        Self._displayName = r["displayName"]

