""" 
This module is used to get the dates of when a game was updated and its subplaces.
A Universe on roblox is what a collection of subplaces and its root place is called!
API DOCS https://create.roblox.com/docs/cloud/legacy/games/v1
SUBPLACE ENDPOINT: https://develop.roblox.com/v2/universes/{universeId}/places
"""

import requests
placeId = 1019367885

response = requests.get(f'https://apis.roblox.com/universes/v1/places/{placeId}/universe') # Get universe ID if none is supplied
json_data = response.json() # Type dictionary

universeID = json_data["universeId"]
response = requests.get(f"https://games.roblox.com/v1/games?universesIds={universeID}")
print(response.json())