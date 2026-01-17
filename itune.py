import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

data = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term="+ sys.argv[1])

o = data.json()

for result in o["results"]:
    print(result["trackName"])

