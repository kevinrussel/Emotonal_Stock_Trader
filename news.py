
## this is newsdata.io 
## look into mediastack???
import http.client,urllib.parse,json
from config import *

conn = http.client.HTTPConnection('api.mediastack.com')

params = urllib.parse.urlencode({
    'access_key': newsAPI,
    'categories': 'general,business,-technology',
    'sort': 'published_desc',
    'languages':'en',
    'countries': 'us',
    'keywords': 'Boeing',
    # 'sources':'elon',
    'limit': 10,
    'date': '2024-10-15'
    })
conn.request('GET', '/v1/news?{}'.format(params))

res = conn.getresponse()
data = res.read()
# print(type(data))
newdata = data.decode('utf-8')
even_newer_data = json.loads(newdata)
# print(even_newer_data)
data_list = even_newer_data['data']
# print(data_list)
for item in data_list:
    print(item['title'])
    print(item['published_at'])
    print(item['source'])
    



# from newsdataapi import NewsDataApiClient
# from config import *

# import json


# api = NewsDataApiClient(apikey=newsAPI)

# query = "Boeing"
# response = api.news_api(q=query)
# data_list = response['results']

# counter = 0
# for item in data_list:
#     counter = counter +1
#     if query in item['title']:
#         print(item['title'])
#         print(item['source_url'])
#         print(item['country'])
    
# print(counter)
    



