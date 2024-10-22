## this will be the main file.
from news import *
from OpenAi import *
# from config import *
from trade import *
import time


## For the stock amount, what we are going to do, is get our number (ex 65) then divide it by 10 to get the number of stocks 
## we are going to buy. ( We should also calculate if we even have enough cash to buy it.)


## this is for tesla.
def teslaFunction():
    BuyTeslaFlag = True
    SellTeslaFlag = True

    TeslaNewsHeadline = ''
    headline = "Tesla"
    newsData = newsHeadline(headline)
    print(newsData[0])
    TeslaNewsHeadline = newsData[0]
    Aiprompt = int(OpenAiPrompt(newsData[0]).content)

    if(Aiprompt>= 60 and SellTeslaFlag == True and "Tesla" in TeslaNewsHeadline):
        BuyTeslaFlag = False ## this is to make sure that we also don't sell the stock if we bought it the same day.
        


## main function.
if __name__ == '__main__':
    try:



        headline= "Tesla"
        newsData = newsHeadline(headline)
        print(newsData[0])
        TeslaNewsHeadline = newsData[0]
        AiPrompt = int(OpenAiPrompt(newsData[0]).content)
        
        if (AiPrompt >=60 and SellTeslaFlag == True and headline): ## this is when we buy. ##TODO fix this so that it is for all the different stocks.
            BuyTeslaFlag= False 
            market_order_request_buy("TSLA",2.5)
            
        elif (AiPrompt <= 40): ## this is when we sell
            print("bye")
        else:
            print("We do nothing.")
        

    
    except Exception as e:
        print(e)
        print("this is an exception")
    



