import requests

url = 'https://nominatim.openstreetmap.org/search'
params = {'format': 'json', 'q': 'dresden'}
headers = {'Referer': 'https://johannesloetzsch.github.io/python-tutorial'}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    ##print(response.json())

    import json
    print(json.dumps(response.json()))
else:
    print(f'Fehler: {response.status_code}\n{response.content}')
