import requests
import sys

payload = {'nTqm': '',
           'lang': 'ru'}

cities = [sys.argv[1]]

for city in cities:
    url_template = 'http://wttr.in/{}'
    url = url_template.format(city)
    response = requests.get(url, params=payload)
    print(response.text)
