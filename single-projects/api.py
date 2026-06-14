import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=5&term=" + sys.argv[1])
name = response.json()

for result in name["results"]:
    print(result["artworkUrl100"])
