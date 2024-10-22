
## this is mediastack.

import http.client,urllib.parse,json
from config import *
conn = http.client.HTTPConnection('api.mediastack.com')

def newsHeadline(keyword):
    params = urllib.parse.urlencode({
        'access_key': newsAPI,
        'categories': 'general,-business,technology',
        'sort': 'popularity', ## sorted it out by popularity.
        'languages':'en',
        'countries': 'us',
        'keywords': keyword,
        'limit': 1, ## since we just one one article to be returned to us.
        'date': '2024-10-20'
        })
    conn.request('GET', '/v1/news?{}'.format(params))

    res = conn.getresponse()
    data = res.read()
    newdata = data.decode('utf-8')
    even_newer_data = json.loads(newdata)
    data_list = even_newer_data['data']
    for item in data_list:
        return item['title'], item['published_at'], item['source']
        






