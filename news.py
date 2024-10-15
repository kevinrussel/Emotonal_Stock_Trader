
## this is newsdata.io 
## look into mediastack???


from newsdataapi import NewsDataApiClient
from config import *

import json


api = NewsDataApiClient(apikey=newsAPI)

query = "Boeing"
response = api.news_api(q=query)
data_list = response['results']

counter = 0
for item in data_list:
    counter = counter +1
    if query in item['title']:
        print(item['title'])
        print(item['source_url'])
        print(item['country'])
    
print(counter)
    



