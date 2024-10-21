
## this is mediastack.

import http.client,urllib.parse,json
from config import *

conn = http.client.HTTPConnection('api.mediastack.com')

params = urllib.parse.urlencode({
    'access_key': newsAPI,
    'categories': 'general,business,-technology',
    'sort': 'popularity', ## sorted it out by popularity.
    'languages':'en',
    'countries': 'us',
    'keywords': 'lasdjla',
    # 'sources':'elon',
    'limit': 1,
    'date': '2024-10-20'
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
    






