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
'''
def create_envelope(customKwargs,*kwargs):
  global dataEnv
  dataEnv = {
    "customFields": {
    "textCustomFields": [
      {
        "name": "CODCOLIGADA",
        "value": ""+CODCOLIGADA+""
      },
      {
        "name": "RA",
        "value": ""+RA+""
      },
      {
        "name": "IDPERLET",
        "value": ""+IDPERLET+""
      },
      {
        "name": "IDHABILITACAOFILIAL",
        "value": ""+IDHABILITACAOFILIAL+""
      },
      {
        "name": "CODCONTRATO",
        "value": ""+CODCONTRATO+""
      },
      
    ]
  },
    "documents": [
      {
        "documentBase64": ""+pdf_64+"",
        "documentId": "99428916",
        "name": "CONTRATO OBJ API PYTHON WITH VAR"
      }
    ],
    "emailSubject": ""+signer_email+"",
    "status": ""+status+"",
    "templateId": ""+template_id+"",
    "templateRoles": [
      {
        "email": ""+cc_email+"",
        "name": ""+cc_name+"",
        "roleName": "Objetivo"
      }
    ]
  }
  return dataEnv
'''
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
          "value": "Lucas Panao"
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

### UPDATE TEMPLATE TABS
update_template()
recipientId = "34859996"
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/templates/{1}/recipients/{2}/tabs'.format(signer_client_id,template_id,recipientId)
response = requests.put(url,json= dataTemplate,headers = hdr)
data = response.json()
with open('custom_tabs.json', 'w') as f:json.dump(data, f)

'''
### CONVERTING PDF INTO BASE64 FILE
with open("contrato-objetivo-2.pdf", "rb") as pdf_file:
    pdf_64 = base64.b64encode(pdf_file.read())
pdf_64 = pdf_64.decode("UTF-8")

### LIST ENVELOPE STATUS
status_env = {"envelopeIds": [""]}
 
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/envelopes?from_date=08/01/2020'.format(signer_client_id)
response = requests.put(url,json= status_env,headers = hdr)
data = response.json()
i = int(data['resultSetSize'])
while i >= 1: 
  print('temos ' + data['resultSetSize'] + ' envelopes enviados')
  for envelopes in data['envelopes']:
    if envelopes['status'] == 'completed':
      print('O envelope ' +envelopes['envelopeId']+ ' foi assinado')  
      i-=1
  print(i)

### CREATING ENVELOPE
CODCOLIGADA = "1";RA = "2";IDPERLET = "3";IDHABILITACAOFILIAL = "4";CODCONTRATO="5"
kwargs = (pdf_64,signer_email,status,template_id,cc_email,cc_name)
customKwargs = (CODCOLIGADA,RA,IDPERLET,IDHABILITACAOFILIAL,CODCONTRATO)
create_envelope(customKwargs,kwargs)
post(url,dataEnv,hdr)

### CREATING ENVELOPE_VIEW 
dataView = {
  "envelopeId" : ""+envelopeId+"",
  "returnUrl" : "https://google.com"
}

url_view = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/views/console'.format(signer_client_id) 
r = requests.post(url_view,json = dataView, headers = hdr)
data = r.json()
envelopeUrl = data['url']
print(envelopeUrl)

### COLLETING TABS FROM ACC 
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/tab_definitions'.format(signer_client_id)
get(url,hdr)
for tabs in data['tabs']:
  tabLabel = (tabs['tabLabel'])
  if tabLabel != '':
    print(tabLabel) 
'''
