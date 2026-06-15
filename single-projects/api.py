import requests
import sys

# checks if the cli argument is enough 
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")

# http get request from the server
response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e14647999e0018b436afce88cfeca71830417bc42650e63825a60bc337cc4394")
# put the response in the price variable and convert it into a float
price = float(response.json()["data"]["priceUsd"])

