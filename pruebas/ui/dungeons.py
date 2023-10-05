import requests
import json

URI = "https://www.dnd5eapi.co/api/classes/?/proficiencies"
response = requests.get(URI)
#print(f"GET:{response.text}")
response_json = json.loads(response.text)
for i in range(12):
    print(f"{i+1}.-{response_json['results'][i]['name']}")


