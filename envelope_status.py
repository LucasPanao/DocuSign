import os
import requests
import yaml
import json
import db_docu

def get(url,hdr):
  global data
  response = requests.get(url, headers = hdr)
  data = response.json()
  with open('envelope.json', 'w') as f:json.dump(data, f)

#### CONFIG
with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
signer_client_id = config['my-config']['clientId']
hdr = config['my-config']['token']
#### END CONFIG

### CALLING DB
db_docu.select = "SELECT * FROM VW_DOCU_ENVELOPES_ENVIADOS_LISTA"
db_docu.select_sql(db_docu.select)

### loop through the envelopes
files = open('ids.txt','r')
for line in files.readlines():
  envelopeId = line.rstrip()
  url = "https://demo.docusign.net/restapi/v2.1/accounts/{0}/envelopes/{1}".format(signer_client_id,envelopeId)
  get(url,hdr)
  print(data['status'])
  if data['status'] != 'sent':
    statusContrato = data['status']
    db_docu.query = '''
                INSERT INTO dbo.DOCU_ENVELOPE_STATUS (DOCU_IDENVELOPE, DOCU_STATUS)
                VALUES
                (?,?)
                    '''
    args = (envelopeId, statusContrato)
    db_docu.insert_sql(db_docu.query,args)