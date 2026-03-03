#Using the API Key from coin-cap to get the latest bit-coin price.
#On the basis of how many bitcoins the user provides via command line argument,
#outputting the updateed exact price to the output buffer.

import sys
import requests
import json

try:
    if len(sys.argv) != 2:
        sys.exit("No value detected.")

    current_data = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=" \
    "53b894acb72bd4ff0eef8be9277eabe37b21efe36d98fc8735f3677372f3c75f")

    current_data = current_data.json()


except requests.RequestException:
    exit()

else:

    price = round(float(current_data["data"]["priceUsd"]), 4)
    print(f"$ {price:,}")






