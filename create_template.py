import os
import requests
import yaml
import json
import pyodbc
from docusign_esign import EnvelopesApi, EnvelopeDefinition, TemplateRole
import base64
import time
from datetime import datetime, timedelta
from docusign_esign.client.api_client import ApiClient


#### START FUNCTIONS
def get(url,hdr):
    global data
    response = requests.get(url, headers = hdr)
    data = response.json()
    with open('envelope.json', 'w') as f:json.dump(data, f)

def post(url,dataEnv,hdr):
  global envelopeId
  r = requests.post(url,json= dataEnv, headers = hdr)
  print(r.json())
  data = r.json()
  envelopeId = data['envelopeId']
  print(envelopeId)
  return envelopeId


def update_template():
  global dataTemplate
  dataTemplate = {
    "textTabs": [
        {
          "tabId": "58cdd9f0-dbdd-46ba-8bc5-1f2371d26f86",
          "tabLabel": "Cidade",
          "value": "Santos"
        },
        {
          "tabId": "c58450a3-1163-4ea7-92fe-f853cc672960",
          "tabLabel": "RG",
          "value": "362.654.12-50"
        },
        {
          "tabId": "5d403fe3-0a80-4a99-8cf9-82177c4a58ce",
          "tabLabel": "Nome Aluno",
          "value": "L Panao"
        },
        {
          "tabId": "e74b0dc4-6112-4abd-8cf9-3870fd321b76",
          "tabLabel": "Unidade",
          "value": "Conselheiro Nebias"
        },
        {
          "tabId": "929a94d6-cb87-4fcb-8d5e-68d1647212a8",
          "tabLabel": "Sexo",
          "value": "Masculino"
        },
        {
          "tabId": "d8fc54ff-c222-41bf-9e25-8de8fa843570",
          "tabLabel": "Local Nascimento",
          "value": "Santos"
        },
        {
          "tabId": "a20d08ae-d5bf-4822-9bfa-b5e0d75fd292",
          "tabLabel": "Nome Resp. Financeiro",
          "value": "Lucas Panao"
        },
        {
          "tabId": "8a7060f1-82f6-4e1b-9379-fd2c7a61658b",
          "tabLabel": "Endereco",
          "value": "R. Conselheiro Nebias 774"
        },
        {
          "tabId": "cf68bd13-d55f-48d8-a6cc-db642df8a227",
          "tabLabel": "Curso",
          "value": "Ensino médio"
        },
        {
          "tabId": "ee51a0cf-ae6c-4fcf-8895-b58d2cb775ff",
          "tabLabel": "CEP",
          "value": "11070-320"
        },
        {
          "tabId": "bc3dedec-0173-4bbc-91f1-ae43f4daaade",
          "tabLabel": "S\u00e9rie",
          "value": "1 ano"
        },
        {
          "tabId": "09052923-efa7-4f84-be76-6c99f2d817f3",
          "tabLabel": "Periodo",
          "value": "noite"
        },
        {
          "tabId": "e1aeb010-0b11-4b13-884d-8524243677fd",
          "tabLabel": "Naturalidade",
          "value": "Brasileiro"
        },
        {
          "tabId": "27ae4bfd-147b-48c9-aad0-dac647d5c12b",
          "tabLabel": "Data Nasc",
          "value": "05/02/1999"
        },
        {
          "tabId": "ba5600bc-41a3-48c2-933f-67415ff0d802",
          "tabLabel": "Tel Recado",
          "value": "33015063"
        },
        {
          "tabId": "a9ee6d8d-bf22-4d89-a590-2b71f08fab17",
          "tabLabel": "Tel R.",
          "value": "33015063"
        },
        {
          "tabId": "1d898afc-e53d-49d8-b281-56082233a79f",
          "tabLabel": "Telefone C.",
          "value": "33015063"
        },
      ]
    }
  return dataTemplate

#### END FUCTIONS   


#### CONFIG
with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
signer_client_id = config['my-config']['clientId']
basepath = config['my-config']['basepath']
token_only = config['my-config']['token_only']
hdr = config['my-config']['token']
status = config['envelope']['status']
template_id = config['envelope']['template_id']
recipient_id = config['template']['recipient_id']
signer_email = config['signer']['email']
signer_name = config['signer']['name']
cc_email = config['cc']['email']
cc_name = config['cc']['name']
#### END CONFIG

update_template()
recipientId = "34859996"
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipientId)
response = requests.put(url,json= dataTemplate,headers = hdr)
data = response.json()
with open('custom_tabs.json', 'w') as f:json.dump(data, f)