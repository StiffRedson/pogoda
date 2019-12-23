import requests

payload = {'nTqm': '',
           'lang': 'ru'}

cities = ['London', 'svo', 'Cherepovets']

for city in cities:
    url_template = 'http://wttr.in/{}'
    url = url_template.format(city)
    response = requests.get(url, params=payload)
    print(response.text)
