## this will be the main file.
from news import *
from OpenAi import *
# from config import *
from trade import *



BuyTeslaFlag = True
SellTeslaFlag = True

TeslaNewsHeadline = ''

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
    
