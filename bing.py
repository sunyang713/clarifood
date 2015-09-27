import pprint
import json
import urllib
import requests
import urlparse

# bing search
BING_KEY = 'bFb7FjpWs3iobGyZSB2iJOyqrCijSOfobHPlhDFYRgI'
DEFAULT_TOP = 10    # default number of search results
OFFSET = 0
BASE_URL = 'https://api.datamarket.azure.com/Bing/Search/Image?$format=json'

# check if url is an image
def image_exists(url):
    try:
        r = requests.get(url)
        print r.headers.get('content-type')
        print r.status_code
        return 'image' in r.headers.get('content-type') and r.status_code == 200
    except requests.exceptions.ConnectionError:
        return False

# returns a list of images according to given query
def image_search(query=None, top=DEFAULT_TOP, offset=OFFSET):
    query = '%27' + urllib.quote_plus(query) + '%27'
    url = BASE_URL + '&Query=%s&$top=%d&$skip=%d' % (query, top, offset)

    response = requests.get(url, auth=(BING_KEY, BING_KEY))
    json_response = json.loads(json.dumps(response.json()))

    results = json_response['d']['results']
    
    images = []
    for data in results:
        if not image_exists(str(data['MediaUrl'])):
            print "doesn't exist"
            continue
        images.append(str(data['MediaUrl']))

    return images

if __name__ == '__main__':
    print image_search(query='bubble tea')