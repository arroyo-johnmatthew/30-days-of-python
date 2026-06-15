import requests
import sys

# checks if the cli argument is enough or too much
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
elif len(sys.argv) > 2:
    sys.exit()

# checks if the command line arg can be converted into a float
try:
    user_bitcoin = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

# http get request from the server using API key
response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e14647999e0018b436afce88cfeca71830417bc42650e63825a60bc337cc4394")
# put the response in the price variable and convert it into a float
price = float(response.json()["data"]["priceUsd"])

# multiply the current bitcoin price usd by the user's bitcoin
price = price * user_bitcoin
print(f"${price:,.4f}", end="")