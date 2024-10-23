# this will be the main file.
from news import *
from OpenAi import *
# from config import *
from trade import *
import time

class main:
    ## For the stock amount, what we are going to do, is get our number (ex 65) then divide it by 10 to get the number of stocks 
    ## we are going to buy. ( We should also calculate if we even have enough cash to buy it.)

    ## This s the constructor, a work in progress but what we have so far.
    def __init__(self):
        self.BuyTeslaFlag = True
        self.SellTeslaFlag = False
        self.TeslaNewsHeadline = "Wall Street Brunch: Tesla Earnings Steal The Spotlight"


    ## this is for tesla.
    def teslaFunction(self):
        headline = "Tesla" ## setting te headline into which we will look for new new's articles.
        newsData = newsHeadline(headline)
        print(newsData[0]) ## printing out the new's articles.

        if(self.TeslaNewsHeadline != newsData[0]): ## we are making sure that we are getting different new's headlines.
            self.TeslaNewsHeadline = newsData[0] ## setting this as the new Headline reference.

            try: ## I am wrapping this in a try catch, because the Ai might return something like 
                ## I'm sorry I can't commment on that ( sometimes this will get thrown becasuse)
                ## the headline has something directly or indirectly related to "classified" or political topics.
                Aiprompt = int(OpenAiPrompt(newsData[0]).content) ## getting the Ai response bac
                print(Aiprompt)

                if(Aiprompt>= 60 and self.SellTeslaFlag == False  and "Tesla" in self.TeslaNewsHeadline):
                    self.BuyTeslaFlag = True ## this is to make sure that we also don't sell the stock if we bought it the same day.
                    
                    ## First step make sure we have enough money to actually buy the stock.
                    stockAmount = (Aiprompt/10) - 5 ## this is so that we can shift the values ( So at most 10 stocks will be bought at a single time.)
                    if(printAccount(stockAmount,"TSLA")== True): ## Making sure the trade was actually sent through.
                        return True
                    else:
                        return False
                elif(Aiprompt <= 40 and self.BuyTeslaFlag == False and "Tesla" in self.TeslaNewsHeadline): ## FIX THE FLAGS.!!!!!!
                    self.SellTeslaFlag = True
                return True
            
            except Exception:
                print("This headline wasn't able to get looked at.")
                return Exception
        elif(self.TeslaNewsHeadline == newsData[0]):
            print("This is the same headline")
            return False

## main function.
if __name__ == '__main__':
    ## creating an instance of the class.
    tesla_instance = main()
    while True: ## We want to loop it continually till the end of the experiment.
        try:
            ## TODO maybe I should multithread so that I can reset the flags every midnight???
            tradeStatus = tesla_instance.teslaFunction()
            if(tradeStatus== True):
                print("There was a successful trade!")
            elif(tradeStatus == False):
                print("It was the same headline!")
            elif(tradeStatus == Exception):
                print("There was an exception raised in main !")
            ## wait 10 minutes.
            time.sleep(50)
            

        
        except Exception as e:
            print(e)
            print("this is an exception")
    



