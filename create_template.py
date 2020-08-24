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
          "tabId": "c0d8c73b-fa10-4b0f-b837-f213c520ddd5",
          "tabLabel": "Cidade",
          "value": "Santos"
        },
        {
          "tabId": "ff3f1e19-0a35-4c27-abc2-97a82e6c9ecb",
          "tabLabel": "RG",
          "value": "362.654.12-50"
        },
        {
          "tabId": "691122e1-158d-4ef6-9c7c-56ab2e6e7bb7",
          "tabLabel": "Nome Aluno",
          "value": "L Panao"
        },
        {
          "tabId": "df6c1d81-98ba-4d60-b13c-c5886d4ba5f5",
          "tabLabel": "Unidade",
          "value": "Conselheiro Nebias"
        },
        {
          "tabId": "a75c73e3-422b-4aa5-9f8f-fd10cc6c54a4",
          "tabLabel": "Sexo",
          "value": "Masculino"
        },
        {
          "tabId": "0176bcc5-bce5-4e93-8abe-35a27cfd8114",
          "tabLabel": "Local Nascimento",
          "value": "Santos"
        },
        {
          "tabId": "a20d08ae-d5bf-4822-9bfa-b5e0d75fd292",
          "tabLabel": "Nome Resp. Financeiro",
          "value": "Lucas Panao"
        },
        {
          "tabId": "f7e9ed6f-019c-43b7-a7ae-28b5ac57d2fd",
          "tabLabel": "Endere\u00e7o",
          "value": "R. Conselheiro Nebias 774"
        },
        {
          "tabId": "0d09fe4c-4bce-4452-b263-24c8086b6c88",
          "tabLabel": "Curso",
          "value": "Ensino médio"
        },
        {
          "tabId": "f4330639-c935-4f47-b966-bdcff568b34d",
          "tabLabel": "CEP",
          "value": "11070-320"
        },
        {
          "tabId": "5ce4531c-cd85-4cb9-bdb5-bd5bab991952",
          "tabLabel": "S\u00e9rie",
          "value": "1 ano"
        },
        {
          "tabId": "6c2f02de-9d6f-4a37-82bd-dd610f259bd7",
          "tabLabel": "Periodo",
          "value": "noite"
        },
        {
          "tabId": "f4d5635a-6f17-4d58-9733-2561840a57f5",
          "tabLabel": "Naturalidade",
          "value": "Brasileiro"
        },
        {
          "tabId": "0253e5d4-dbc9-4eab-aa3d-3117a949c3a2",
          "tabLabel": "Data Nasc",
          "value": "05/02/1999"
        },
        {
          "tabId": "9d82230f-c28f-4801-8372-2c5bd8233adf",
          "tabLabel": "Tel Recado",
          "value": "33015063"
        },
        {
          "tabId": "11a39b1a-ddb9-416f-babf-18b77c22d097",
          "tabLabel": "Telefone C.",
          "value": "33015063"
        },
        {
          "tabId": "f5ba33d0-dead-4418-bc36-6923c08da655",
          "tabLabel": "UF",
          "value": "SP"
        },
        {
          "tabId": "04ca7fcb-1816-49ae-8980-c903bb0598f5",
          "tabLabel": "Bairro",
          "value": "Embare"
        },
        {
          "tabId": "2c835c90-b02b-478e-afb1-112a64def3a6",
          "tabLabel": "Pai",
          "value": "Lucas Panao Pai"
        },
        {
          "tabId": "056fe630-a7e8-440c-8969-e7e4848059c8",
          "tabLabel": "Mae",
          "value": "Lucas Panao Mae"
        },
        {
          "tabId": "146e30de-3592-476d-950a-0becb477dec8",
          "tabLabel": "RA",
          "value": "123456"
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
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipient_id)
response = requests.put(url,json= dataTemplate,headers = hdr)
data = response.json()
with open('custom_tabs.json', 'w') as f:json.dump(data, f)