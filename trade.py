
from config import*
# from alpaca.broker.client import BrokerClient
# from alpaca.trading.client import TradingClient
import requests,json
# BASE_URL = "https://paper-api.alpaca.markets/v2/account"
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


## TODO: make sure that we find a way to ensure that if we are selling a stock, we already have some already, and the qty we have is greater than or equal to the 
## amount we are selling. 


## TODO: Find a way to ensure that we have a specific stock. 
def printAccount():
    print('${} is available as cash.'.format(account))
    print(trading_client.get_open_position("TSLA")) ## this is to check the current price of how much I bought of tesla.
def market_order_request_buy(symbol,qty):
    market_order_data = MarketOrderRequest(
        symbol = symbol,
        qty = qty,
        side = OrderSide.BUY,
        time_in_force = TimeInForce.DAY
    )
    market_order(market_order_data)


def market_order_request_sell(symbol,qty):
    market_order_data = MarketOrderRequest(
        symbol = symbol,
        qty = qty,
        side = OrderSide.SELL,
        time_in_force = TimeInForce.DAY
    )
    market_order(market_order_data)

def market_order( market_order_data):
    market_order = trading_client.submit_order(order_data = market_order_data)

printAccount()