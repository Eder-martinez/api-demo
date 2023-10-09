import requests
import json

URI = "https://www.dnd5eapi.co/api/classes"
response = requests.get(URI)
#print(f"GET:{response.text}")
response_json = json.loads(response.text)
for i in range(12):
    print(f"{i+1}.-{response_json['results'][i]['name']}")
personaje = int(input("Elije uno de los personajes para poder ver las caracteristicas: "))

if personaje == 1:
    URI = "https://www.dnd5eapi.co/api/classes/barbarian/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(7):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 2:
    URI = "https://www.dnd5eapi.co/api/classes/bard/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(8):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 3:
    URI = "https://www.dnd5eapi.co/api/classes/cleric/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(6):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 4:
    URI = "https://www.dnd5eapi.co/api/classes/druid/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(16):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 5:
    URI = "https://www.dnd5eapi.co/api/classes/fighter/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(6):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 6:
    URI = "https://www.dnd5eapi.co/api/classes/monk/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(4):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 7:
    URI = "https://www.dnd5eapi.co/api/classes/paladin/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(6):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 8:
    URI = "https://www.dnd5eapi.co/api/classes/ranger/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(7):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 9:
    URI = "https://www.dnd5eapi.co/api/classes/rogue/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(9):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 10:
    URI = "https://www.dnd5eapi.co/api/classes/sorcerer/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(7):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 11:
    URI = "https://www.dnd5eapi.co/api/classes/warlock/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(4):
        print(f"{i+1}.-{response_json['results'][i]['name']}")

elif personaje == 12:
    URI = "https://www.dnd5eapi.co/api/classes/wizard/proficiencies"
    response = requests.get(URI)
    #print(f"GET:{response.text}")
    response_json = json.loads(response.text)
    for i in range(7):
        print(f"{i+1}.-{response_json['results'][i]['name']}")
else:
    print("Elije algo valido")
