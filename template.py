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
import start_var


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

def put():
  url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipient_id)
  requests.put(url,json= dataTemplate,headers = hdr)
  print('criado com sucesso')

def update_template():
  global dataTemplate
  dataTemplate = {
    "textTabs": [
        {
          "tabId": "c0d8c73b-fa10-4b0f-b837-f213c520ddd5",
          "tabLabel": "Cidade",
          "value": ""+start_var.CIDADE[0]+""
        },
        {
          "tabId": "ff3f1e19-0a35-4c27-abc2-97a82e6c9ecb",
          "tabLabel": "RG",
          "value": ""+start_var.RG[0]+""
        },
        {
          "tabId": "691122e1-158d-4ef6-9c7c-56ab2e6e7bb7",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[0]+""
        },
        {
          "tabId": "df6c1d81-98ba-4d60-b13c-c5886d4ba5f5",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE[0]+""
        },
        {
          "tabId": "a75c73e3-422b-4aa5-9f8f-fd10cc6c54a4",
          "tabLabel": "Sexo",
          "value": ""+start_var.SEXO[0]+""
        },
        {
          "tabId": "0176bcc5-bce5-4e93-8abe-35a27cfd8114",
          "tabLabel": "Local Nascimento",
          "value": ""+start_var.LOCALNASC[0]+""
        },
        {
          "tabId": "a20d08ae-d5bf-4822-9bfa-b5e0d75fd292",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[0]+""
        },
        {
          "tabId": "f7e9ed6f-019c-43b7-a7ae-28b5ac57d2fd",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[0]+""
        },
        {
          "tabId": "0d09fe4c-4bce-4452-b263-24c8086b6c88",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO[0]+""
        },
        {
          "tabId": "f4330639-c935-4f47-b966-bdcff568b34d",
          "tabLabel": "CEP",
          "value": ""+start_var.CEP[0]+""
        },
        {
          "tabId": "5ce4531c-cd85-4cb9-bdb5-bd5bab991952",
          "tabLabel": "S\u00e9rie",
          "value": ""+start_var.SERIE[0]+""
        },
        {
          "tabId": "6c2f02de-9d6f-4a37-82bd-dd610f259bd7",
          "tabLabel": "Periodo",
          "value": ""+start_var.PERIODO[0]+""
        },
        {
          "tabId": "f4d5635a-6f17-4d58-9733-2561840a57f5",
          "tabLabel": "Naturalidade",
          "value": ""+start_var.NATURALIDADE[0]+""
        },
        {
          "tabId": "0253e5d4-dbc9-4eab-aa3d-3117a949c3a2",
          "tabLabel": "Data Nasc",
          "value": ""+start_var.DATANASC[0]+""
        },
        {
          "tabId": "9d82230f-c28f-4801-8372-2c5bd8233adf",
          "tabLabel": "Tel Recado",
          "value": ""+start_var.TELR[0]+""
        },
        {
          "tabId": "11a39b1a-ddb9-416f-babf-18b77c22d097",
          "tabLabel": "Telefone C.",
          "value": ""+start_var.TELC[0]+""
        },
        {
          "tabId": "f5ba33d0-dead-4418-bc36-6923c08da655",
          "tabLabel": "UF",
          "value": ""+start_var.UF[0]+""
        },
        {
          "tabId": "04ca7fcb-1816-49ae-8980-c903bb0598f5",
          "tabLabel": "Bairro",
          "value": ""+start_var.BAIRRO[0]+""
        },
        {
          "tabId": "2c835c90-b02b-478e-afb1-112a64def3a6",
          "tabLabel": "Pai",
          "value": ""+start_var.PAI[0]+""
        },
        {
          "tabId": "056fe630-a7e8-440c-8969-e7e4848059c8",
          "tabLabel": "Mae",
          "value": ""+start_var.MAE[0]+""
        },
        {
          "tabId": "146e30de-3592-476d-950a-0becb477dec8",
          "tabLabel": "RA",
          "value": ""+start_var.RA_ALUNO[0]+""
        },
        ## MATERIAL DIDÁTICO ##
        ## MATERIAL DIDÁTICO ##
        {
          "tabId": "4b56506d-f591-4122-a6b0-c5c4557b7486",
          "tabLabel": "Cidade",
          "value": ""+start_var.CIDADE[0]+""
        },
        {
          "tabId": "039825b0-454f-4773-8b42-e49a55d26cdf",
          "tabLabel": "RG",
          "value": ""+start_var.RG[0]+""
        },
        {
          "tabId": "7b75e723-4476-4a1f-9cc5-34d9cca3cde4",
          "tabLabel": "Nome Aluno",
          "value": ""+start_var.NOMEALUNO[0]+""
        },
        {
          "tabId": "6d16db9f-7f37-4713-b239-a517b8419660",
          "tabLabel": "Unidade",
          "value": ""+start_var.UNIDADE[0]+""
        },
        {
          "tabId": "b0bd9d74-1963-4bee-9f92-64a8708ab11a",
          "tabLabel": "Endere\u00e7o",
          "value": ""+start_var.ENDERECO[0]+""
        },
        {
          "tabId": "df92885b-9b5b-4fe7-868d-7704a6dbe84b",
          "tabLabel": "CEP",
          "value": ""+start_var.CEP[0]+""
        },
        {
          "tabId": "706a49ef-09d5-44ff-a111-32014bfcdaa4",
          "tabLabel": "S\u00e9rie",
          "value": ""+start_var.SERIE[0]+""
        },
        {
          "tabId": "471aa8f2-7d7e-43d5-b6df-5809d9a1fe6a",
          "tabLabel": "UF",
          "value": ""+start_var.UF[0]+""
        },
        {
          "tabId": "06543537-50b4-42cb-be50-8aa6b35a9de9",
          "tabLabel": "Bairro",
          "value": ""+start_var.BAIRRO[0]+""
        },
        {
          "tabId": "8614728c-e722-436f-8cb2-b7fe5ccbbb3a",
          "tabLabel": "Pai",
          "value": ""+start_var.PAI[0]+""
        },
        {
          "tabId": "9c811b5b-aa2e-4750-ba1b-85f598ca189c",
          "tabLabel": "Mae",
          "value": ""+start_var.MAE[0]+""
        },
        {
          "tabId": "f750ead6-0d19-4bfa-9e39-3bc9ef606885",
          "tabLabel": "RA",
          "value": ""+start_var.RA_ALUNO[0]+""
        },
        {
          "tabId": "9fbc4b26-1c0b-4c59-8dde-f9b687fd2aa8",
          "tabLabel": "Curso",
          "value": ""+start_var.CURSO[0]+""
        },
        {
          "tabId": "260e42a3-fdb0-4278-8f70-6db362e410e0",
          "tabLabel": "Periodo",
          "value": ""+start_var.PERIODO[0]+""
        },
        {
          "tabId": "94d2888b-573a-4496-97f5-9457f70f6685",
          "tabLabel": "Nome Resp. Financeiro",
          "value": ""+start_var.NOMERESPF[0]+""
        },
        {
          "tabId": "aefef120-9085-4bde-90c1-4c009705a730",
          "tabLabel": "Telefone C.",
          "value": ""+start_var.TELC[0]+""
        },
        {
          "tabId": "8ca3a87b-299c-4f21-a27b-aef64582cd97",
          "tabLabel": "CPF",
          "value": ""+start_var.CPF[0]+""
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

'''
start_var.start_variables_template()
update_template()
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipient_id)
response = requests.put(url,json= dataTemplate,headers = hdr)
data = response.json()
with open('custom_tabs.json', 'w') as f:json.dump(data, f)
'''