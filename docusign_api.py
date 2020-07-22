import os
import requests
import yaml
import json

with open('config.yml') as c:
    config = yaml.load(c)
url = config['my-config']['url']
hdr = config['my-config']['token']

response = requests.get(url, headers = hdr)
data = response.json()
print (data)