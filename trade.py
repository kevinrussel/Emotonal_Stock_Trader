
from config import*
# from alpaca.broker.client import BrokerClient
# from alpaca.trading.client import TradingClient
import requests,json
# BASE_URL = "https://paper-api.alpaca.markets/v2/account"

# HEADERS = {'APCA-API-KEY-ID':APIKEY,'APCA-API-SECRET-KEY':SECRET_API_KEY}

# def GETINFO():
#     r = requests.get(BASE_URL, headers=HEADERS)
#     return r.content
    
# # print(GETINFO())
# # gets the info as bytes
# response_bytes = GETINFO()
# ## decode the bytes into a stringclearclear

# response = response_bytes.decode("utf-8")
# ## loads the string into a python dict
# data = json.loads(response)
# for keys,value in data:
#     print(keys,value )
# # getting the key value pair
# buying_power = data["buying_power"]
# print(f"The buying power is: {buying_power}")

from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
trading_client = TradingClient(APIKEY, SECRET_API_KEY)

# Get our account information.
account = trading_client.get_account()

# Check if our account is restricted from trading.
if account.trading_blocked:
    print('Account is currently restricted from trading.')

# Check how much money we can use to open new positions.
print('${} is available as buying power.'.format(account.buying_power))

market_order_request = MarketOrderRequest(
    symbol = "NVDA",
    qty = 1.0,
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY
)

market_order = trading_client.submit_order(

    order_data=market_order_request
)   