import os
import yaml
import pyodbc

with open('config.yml') as f:
    db_config = yaml.load(f)
server = db_config['db-config']['server']
database = db_config['db-config']['database']
username = db_config['db-config']['username']
password = db_config['db-config']['password']

def retornar_conexao_sql():
    #username = ""
    #password = ""
    #string_conexao = 'Driver={ODBC DRIVER 17 for SQL Server};Server='+server+';Database='+database+';UID='+username+';PWD='+ password
    string_conexao = 'Driver={ODBC DRIVER 17 for SQL Server};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()

cursor = retornar_conexao_sql()
cursor.execute("SELECT * FROM tb_alunos")
row = cursor.fetchone()
if row:
    print(row)