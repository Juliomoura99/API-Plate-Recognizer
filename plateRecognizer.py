# pip install requests
import requests
#from pprint import pprint
import json
import sys


regions = ['br'] # Change to your country

with open('', 'rb') as fp:      # Colocar o caminho que leva ao snapshot do carro
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': 'Token MyToken'})

plate_num = response.json()['results'][0]['plate']

print(plate_num)
