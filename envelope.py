import os
import requests
import yaml
import json
import pyodbc
import base64
import time
from datetime import datetime, timedelta
import db_docu
import start_var


#### START FUNCTIONS
def get(url,hdr):
    global data
    response = requests.get(url, headers = hdr)
    data = response.json()
    with open('envelope.json', 'w') as f:json.dump(data, f)

def post(url,dataEnv,hdr):
  global envelopeId
  global statusContrato
  r = requests.post(url,json= dataEnv, headers = hdr)
  print(r.json())
  data = r.json()
  envelopeId = data['envelopeId']
  statusContrato = data['status']
  print(envelopeId)
  return envelopeId, statusContrato

def create_envelope(i,customKwargs,*kwargs):
  global dataEnv
  dataEnv = {
    "customFields": {
    "textCustomFields": [
      {"name": "CODCOLIGADA","value": ""+start_var.CODCOLIGADA[i]+""},
      {"name": "RA","value": ""+start_var.RA[i]+""},
      {"name": "IDPERLET","value": ""+start_var.IDPERLET[i]+""},
      {"name": "IDHABILITACAOFILIAL","value": ""+start_var.IDHABILITACAOFILIAL[i]+""},
      {"name": "CODCONTRATO","value": ""+start_var.CODCONTRATO[i]+""},      
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

### GRAVANDO NO BANCO
def gravar(i):
  db_docu.query = '''
                  INSERT INTO dbo.DOCU_ENVELOPE (DOCU_IDENVELOPE, TOTVS_CODCOLIGADA, TOTVS_IDHABILITACAOFILIAL, TOTVS_IDPERLET, TOTVS_RA, TOTVS_CODCONTRATO)
                  VALUES
                  (?,?,?,?,?,?)
                      '''
  args = (envelopeId, start_var.CODCOLIGADA[i],start_var.RA[i],start_var.IDPERLET[i],start_var.IDHABILITACAOFILIAL[i],start_var.CODCONTRATO[i])
  print(args)
  db_docu.insert_sql(db_docu.query,args)


  db_docu.query = '''
                  INSERT INTO dbo.DOCU_ENVELOPE_STATUS (DOCU_IDENVELOPE, DOCU_STATUS)
                  VALUES
                  (?,?)
                      '''
  args = (envelopeId, statusContrato)
  db_docu.insert_sql(db_docu.query,args)

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
with open("contrato-completo.pdf", "rb") as pdf_file:
    pdf_64 = base64.b64encode(pdf_file.read())
pdf_64 = pdf_64.decode("UTF-8")

### CREATING ENVELOPE
def create_var_envelope(i):
  global kwargs
  global customKwargs
  ## INICIA OS ARRAYS COM AS INFOS DO BANCO PARA O ENVELOPE
  start_var.start_variables_envelope()
  kwargs = (pdf_64,signer_email,status,template_id,cc_email,cc_name)
  customKwargs = (start_var.CODCOLIGADA[i],start_var.RA[i],start_var.IDPERLET[i],start_var.IDHABILITACAOFILIAL[i],start_var.CODCONTRATO[i])


