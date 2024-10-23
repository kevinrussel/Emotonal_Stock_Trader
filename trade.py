
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
def printAccount(qty,symbol):
    ##TODO make sure that we deal with selling as well !!!!.
    
    
    # portfolio = trading_client.get_all_positions()
    try:
        total_cash =float (account.cash)
        print('${} is available as cash.'.format(total_cash))
        StockPrice = trading_client.get_open_position(symbol) ## this is to check the current price of how much I bought of tesla.
        currentPrice = float(StockPrice.current_price)
        print(currentPrice)
        print("This will be the total cost of the trade roughly ~~ ")
        order_price = currentPrice * qty + 2 # The plus two is acting as a buffer between the time order is looked at and order is palced, there might be a price movement.
        print(order_price)
        print(type(order_price))
        print(type(total_cash))
        if(order_price <= total_cash):
            try:
                market_order_request_buy(symbol,qty)
                return True
            except Exception as E:
                print("There was an exception is sending the marketrequestorder in printAccount")
                print(E)
                return False 

    except Exception as e:
        print("There is an error in printAccount.")
        print(e)
        return False


def market_order_request_buy(symbol,quantity):
    market_order_data = MarketOrderRequest(
        symbol = symbol,
        qty = quantity,
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
    print("Market order has been sent through")


# def calculateAmount(qty,symbol):


    