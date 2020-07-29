import os
import requests
import yaml
import json
import pyodbc

#### Funções
def request(url,hdr):
    global data
    response = requests.get(url, headers = hdr)
    data = response.json()

def retornar_conexao_sql():
    global conexao
    string_conexao = 'Driver={ODBC DRIVER 17 for SQL Server};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()
####

with open('config.yml') as c:
    config = yaml.safe_load(c)
url = config['my-config']['url']
hdr = config['my-config']['token']
server = config['db-config']['server']
database = config['db-config']['database']
username = config['db-config']['username']
password = config['db-config']['password']


request(url,hdr)

for envlp in data['envelopes']:
    envlpId = (envlp['envelopeId'])
    envlpSts = (envlp['status']) 
    envlpDate = (envlp['completedDateTime'])
print(envlpId,envlpSts,envlpDate)

url = url.split('?') # divide os parametros passados na URL 

url = url[0] + '/' + envlpId + '/recipients' #cria a url para encontrar os dados do recebedor

request(url,hdr)

for signers in data['signers']:
    s_name = (signers['name'])
    s_email = (signers['email'])
    s_recipientId = (signers['recipientId'])
print(s_name,s_email,s_recipientId)

cursor = retornar_conexao_sql()
cursor.execute("SELECT * FROM Integra_DocuSign")
cursor.execute('''
                INSERT INTO Integra_DocuSign (id_envelope, status_assinatura, data_assinatura, id_recipiente, email, nome)
                VALUES
                (?,?,?,?,?,?);
                ''',envlpId ,envlpSts ,envlpDate ,s_recipientId ,s_email ,s_name)
conexao.commit()

with open('contrato.json', 'w') as f:json.dump(data, f)