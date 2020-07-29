import os
import requests
import yaml
import json

def request(url,hdr):
    global data
    response = requests.get(url, headers = hdr)
    data = response.json()

with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
hdr = config['my-config']['token']

request(url,hdr)

for envlp in data['envelopes']:
    envlpId = (envlp['envelopeId'])
    envlpSts = (envlp['status']) 
    envlpCompl = (envlp['completedDateTime'])
print(envlpId,envlpSts,envlpCompl)

url = url.split('?') # divide os parametros passados na URL 

url = url[0] + '/' + envlpId + '/recipients' #cria a url para encontrar os dados do recebedor

request(url,hdr)

for signers in data['signers']:
    s_name = (signers['name'])
    s_email = (signers['email'])
    s_recipientId = (signers['recipientId'])
print(s_name,s_email,s_recipientId)

with open('contrato.json', 'w') as f:json.dump(data, f)