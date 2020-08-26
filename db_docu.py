import os
import yaml
import pyodbc

with open('config.yml') as f:
    db_config = yaml.safe_load(f)
server = db_config['db-config']['server']
database = db_config['db-config']['database']
username = db_config['db-config']['username']
password = db_config['db-config']['password']

def retornar_conexao_sql():
    global conexao
    string_conexao = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()

def select_sql(select):
    global row
    abre_arq()
    cursor = retornar_conexao_sql()
    cursor.execute(select)
    for row in cursor.fetchall():
        print(row)
        salva_arq(ids)

def insert_sql(query,args):
    cursor = retornar_conexao_sql()
    cursor.execute(query,args)
    conexao.commit()
    print('gravado no banco')

def abre_arq():
    global ids
    ids = open('ids.txt','w')

def salva_arq(ids):
    ids.write(str(row) + "\n")

select = "SELECT * FROM VW_DOCU_ENVELOPES_ENVIADOS_LISTA"
select_sql(select)
                  