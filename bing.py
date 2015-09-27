import pprint
import json
import urllib
import requests

# bing search
BING_KEY = 'bFb7FjpWs3iobGyZSB2iJOyqrCijSOfobHPlhDFYRgI'
DEFAULT_TOP = 10    # default number of search results
OFFSET = 0
BASE_URL = 'https://api.datamarket.azure.com/Bing/Search/Image?$format=json'


# returns a list of images according to given query
def image_search(query=None, top=DEFAULT_TOP):
    query = '%27' + urllib.quote_plus(query) + '%27'
    url = BASE_URL + '&Query=%s&$top=%d&$skip=%d' % (query, top, OFFSET)

    response = requests.get(url, auth=(BING_KEY, BING_KEY))

    results = json.loads(json.dumps(response.json()))['d']['results']
    
    images = []
    for data in results:
        images.append(str(data['MediaUrl']))

    return images

if __name__ == '__main__':
    print image_search(query='bubble tea')