#Using the API Key from coin-cap to get the latest bit-coin price.
#On the basis of how many bitcoins the user provides via command line argument,
#outputting the updateed exact price to the output buffer.

import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit(print("Enter atleast one value: "))
    
