import json
with open('character.json') as f:
    data = json.load(f)
planet = data.get("origin")
print(data.get("name",))
print(planet["name"])
print(data.get("episode"))