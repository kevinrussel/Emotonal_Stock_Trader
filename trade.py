
from config import *
import requests,json
BASE_URL = "https://paper-api.alpaca.markets/v2/account"

HEADERS = {'APCA-API-KEY-ID':APIKEY,'APCA-API-SECRET-KEY':SECRET_API_KEY}

def GETINFO():
    r = requests.get(BASE_URL, headers=HEADERS)
    return r.content
    
print(APIKEY)
print(SECRET_API_KEY)
print(BASE_URL)
print(GETINFO())