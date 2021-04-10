"""
Google command line script for search query with google API
"""

import urllib
from urllib.request import urlopen
import json


url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"
url = "https://developers.google.com/custom-search/"
query = urllib.parse.urlencode({'q': input("What do you want to search for ? >> ")})

response = urlopen(url + query).read()
data = json.loads(response)
print(data)
results = data['responseData']['results']

for result in results:
    title = result['title']
    url = result['url']
    print(title +  ";" + url)
