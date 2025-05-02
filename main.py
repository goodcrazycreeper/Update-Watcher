import modules.universe as universe

# universe.getUniverseData(124180448122765)
placeid = 124180448122765
print(universe.getMethod(f'https://apis.roblox.com/universes/v1/places/{placeid}/universe')["data"]["universeId"])
print(universe.getUniverseData(124180448122765))