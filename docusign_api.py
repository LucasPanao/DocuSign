import os
import requests
import yaml
import json

with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
hdr = config['my-config']['token']

response = requests.get(url, headers = hdr)
data = response.json()

for envlp in data['envelopes']:
    envlpId = (envlp['envelopeId'])
    envlpSts = (envlp['status']) 
    envlpCompl = (envlp['completedDateTime'])
print(envlpId,envlpSts,envlpCompl)

with open('info_contrato.json', 'w') as f:json.dump(data, f)