# reqmethods.py
"""
# Universe.py\nResponsible for retrieving universe data such as number of subplaces.
Contains helper functions and methods for API calls
"""
import requests


def CheckKeyExists(dict, key):
    """Ensures that a key exists before accessing the given key."""
    if dict != None:
        return key in dict  # Check if the 'address' key exists in the dictionary
    else:
        return False


def GetMethod(*args, Debug: bool = False, **kwargs):  # Returns dictionary: "data"
    """Wraps a get request in a try statement. Returns a dictionary, Dictionary is optional, where debug is false pass json data from get()

    :param Debug: Tweak return statement to either wrap data from get into a dictionary or not
    :returnd Dict: If an exception occurs, where and if an exception occurs while Debug is True, returns "data" as None and status code as -1.
    Returns a dictionary, where "data" is the json from the GET request method and status is the status code of the GET method.
    """
    try:
        Response = requests.get(*args, timeout=30, **kwargs)
    except Exception as e:
        print(f"exception as: {e} in {__name__}")
        if Debug == True:
            return None
        else:
            return {"data": None, "status": -1}  # Return none when error occurs
    if Debug == True:
        return Response.json()
    else:
        return {"data": Response.json(), "status": Response.status_code}


def GetUniverseId(PlaceId) -> int:
    """# GetUniverseId:
    Retrieves UniverseID and returns it as a pure integer.\n
    Returns -1 if the universeId field does not exist.
    """
    # Dependencies: GetMethod, CheckKeyExists.
    Response = GetMethod(
        f"https://apis.roblox.com/universes/v1/places/{PlaceId}/universe", Debug=True
    )
    if CheckKeyExists(Response, "universeId") == True:
        Response = Response["universeId"]
        if Response != "null":
            return Response
    else:
        return -1  # Return if universeId does not exist


def GetUniverseData(PlaceId):
    """Method to retrieve a JSON about a roblox Universe"""
    Response = GetUniverseId(PlaceId)
    if Response == -1:
        raise Exception("Universe Field does not exist")
    return GetMethod(f"https://develop.roblox.com/v2/universes/{Response}/places")
