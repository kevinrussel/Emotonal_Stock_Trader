## this will be the main file.
from news import *
from OpenAi import *
# from config import *
# from trade import *






if __name__ == '__main__':
    try:
        newsData = newsHeadline("Tesla")
        print(newsData[0])
        AiPrompt = int(OpenAiPrompt(newsData[0]).content)
        
        if(AiPrompt >=60): ## this is when we buy.
            print("hi")
        elif (AiPrompt <= 40): ## this is when we sell
            print("bye")
        else:
            print("We do nothing.")
        

    
    except Exception as e:
        print(e)
        print("this is an exception")
    
