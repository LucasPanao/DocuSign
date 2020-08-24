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

### CONVERTING PDF TO BASE64
with open("contrato-objetivo-2.pdf", "rb") as pdf_file:
    pdf_64 = base64.b64encode(pdf_file.read())
pdf_64 = pdf_64.decode("UTF-8")


### CREATING ENVELOPE
CODCOLIGADA = "1";RA = "2";IDPERLET = "3";IDHABILITACAOFILIAL = "4";CODCONTRATO="5"
kwargs = (pdf_64,signer_email,status,template_id,cc_email,cc_name)
customKwargs = (CODCOLIGADA,RA,IDPERLET,IDHABILITACAOFILIAL,CODCONTRATO)
create_envelope(customKwargs,kwargs)
post(url,dataEnv,hdr)