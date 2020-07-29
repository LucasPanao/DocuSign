import os
import yaml
import pyodbc

with open('config.yml') as f:
    db_config = yaml.safe_load(f)
server = db_config['db-config']['server']
database = db_config['db-config']['database']
username = db_config['db-config']['username']
password = db_config['db-config']['password']
valor_id = '12345'

def retornar_conexao_sql():
    global conexao
    #username = ""
    #password = ""
    #string_conexao = 'Driver={ODBC DRIVER 17 for SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={ODBC DRIVER 17 for SQL Server};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()

cursor = retornar_conexao_sql()
cursor.execute("SELECT * FROM Integra_DocuSign")
cursor.execute('''
                INSERT INTO Integra_DocuSign (id_envelope)
                VALUES
                (?)
                ''', valor_id)
conexao.commit()