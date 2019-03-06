import requests
import base64
import json
from datetime import datetime

BASE_URL = 'https://api.nbiot.telenor.io/'
collection_id = '17dh0cf43jfk96'
device_id = '17dh0cf43jfn0j'

with open('../api-token.txt') as f:
    api_token = f.read()

headers = {'X-API-Token': api_token}


url = f'{BASE_URL}collections/{collection_id}/devices/{device_id}/data'
response = requests.get(url, params={'limit': 100000}, headers=headers)

messages = response.json()['messages']
messages.reverse()

with open('data/data.csv', 'w') as f:
    f.write('time,co2,tvoc\n')

    for message in messages:
        timestamp = message['received'] // 1000
        isotime = datetime.fromtimestamp(timestamp).isoformat()
        payload = message['payload']
        payload_string = base64.b64decode(payload)
        try:
            payload_json = json.loads(payload_string)
        except json.JSONDecodeError:
            continue

        co2 = payload_json['co2']
        tvoc = payload_json['tvoc']

        f.write(f'{isotime},{co2},{tvoc}\n')
