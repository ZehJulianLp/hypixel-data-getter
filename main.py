import requests
import json
while True:
    uuid = input("UUID, Player Name or exit: ")
    if uuid == "exit":
        print("Exiting Program...")
        break
    else:
        try:
            mojanduuid = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{uuid}").json()
            print("")
            uuid1 = mojanduuid['id']
            apikey = "Put Hypixel API-Key into here"
            r = requests.get(f"https://api.hypixel.net/player?key={apikey}&uuid={uuid1}")
            print("")
            jsonr = r.json()
            out = json.dumps(jsonr, indent=4, sort_keys=True)
            print(out)
            with open("data.json", "w") as file:
                file.write(out)
        except:
            print("Error. Please enter a valid name, UUID or exit.")