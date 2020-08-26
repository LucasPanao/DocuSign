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
import db_docu

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

### CALLING DB
'''
db_docu.select = "SELECT * FROM VW_DOCU_ENVELOPES_ENVIADOS_LISTA"
db_docu.select_sql(db_docu.select)

'''
request_body = {
  "envelopeIds": [
    "",
    ""
    ]
  }
 
url = 'https://demo.docusign.net/restapi/v2.1/accounts/{0}/envelopes/status?envelope_ids=request_body'.format(signer_client_id)
response = requests.put(url,json=request_body,headers = hdr)
data = response.json()
with open('status.json', 'w') as f:json.dump(data, f)
'''
i = int(data['resultSetSize'])
while i >= 1: 
  print('temos ' + data['resultSetSize'] + ' envelopes enviados')
  for envelopes in data['envelopes']:
    if envelopes['status'] == 'completed':
      print('O envelope ' +envelopes['envelopeId']+ ' foi assinado')  
      i-=1
  print(i)
'''