import requests


url = "http://47.237.106.32:8000/pokemon_effect/"


for pokemon_ability_id in range(1,1000):
    
    payload = {
        "pokemon_ability_id": str(pokemon_ability_id)
    }

    try:
       
        response = requests.post(url, json=payload)
        

        if response.status_code == 200:
            print(f"Successfully processed pokemon_ability_id: {pokemon_ability_id}")
            print(response.json())
        else:
            print(f"Failed to process pokemon_ability_id: {pokemon_ability_id}")
            print(response.status_code, response.text)
    
    except Exception as e:
        print(f"Exception occurred for pokemon_ability_id: {pokemon_ability_id}")
        print(str(e))
