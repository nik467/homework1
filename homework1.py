import json
with open("users.json") as f:
    data = json.load(f)
    
result = {z["address"]["city"]: z["name"] for z in data}

with open("cities.json","w", encoding='utf-8') as f:
     json.dump(result, f, indent=4)
