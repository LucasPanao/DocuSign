import os
import requests
import yaml
import json
import pyodbc
from docusign_esign import EnvelopesApi, EnvelopeDefinition, TemplateRole
from consts import pattern
from flask import request, session
import base64


#### START FUNCTIONS
def requested(url,hdr):
    global data
    response = requests.get(url, headers = hdr)
    data = response.json()

def get_args(*kwargs):
        global args
        global envelope_args
        envelope_args = {
            "signer_email": signer_email,
            "signer_name": signer_name,
            "cc_email": cc_email,
            "cc_name": cc_name,
            "template_id": template_id
        }
        args = {
            "account_id": signer_client_id,
            "base_path": basepath,
            "access_token": token_only,
            "envelope_args": envelope_args
        }
        return args

def make_envelope(args):
        """
        Creates envelope
        args -- parameters for the envelope:
        signer_email, signer_name, signer_client_id
        returns an envelope definition
        """
        global envelope_definition
        # create the envelope definition
        envelope_definition = EnvelopeDefinition(
            status="sent",  # requests that the envelope be created and sent.
            template_id=args["template_id"]
        )
        # Create template role elements to connect the signer and cc recipients
        # to the template
        signer = TemplateRole(
            email=args["signer_email"],
            name=args["signer_name"],
            role_name="signer"
        )
        # Create a cc template role.
        cc = TemplateRole(
            email=args["cc_email"],
            name=args["cc_name"],
            role_name="cc"
        )

        # Add the TemplateRole objects to the envelope object
        envelope_definition.template_roles = [signer, cc]
        return envelope_definition

#### END FUCTIONS   

with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
signer_client_id = config['my-config']['clientId']
basepath = config['my-config']['basepath']
token_only = config['my-config']['token_only']
hdr = config['my-config']['token']
status = config['envelope']['status']
template_id = config['envelope']['template_id']
signer_email = config['signer']['email']
signer_name = config['signer']['name']
cc_email = config['cc']['email']
cc_name = config['cc']['name']

### CONVERTING PDF INTO BASE64 FILE
with open("contrato-objetivo-2.pdf", "rb") as pdf_file:
    pdf_64 = base64.b64encode(pdf_file.read())
pdf_64 = pdf_64.decode("UTF-8")

dataEnv = {
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


kwargs = (signer_email,signer_name,cc_email,cc_name,template_id,signer_client_id,basepath,token_only)
get_args(kwargs)

r = requests.post(url,json= dataEnv, headers = hdr)
print(r.json())
