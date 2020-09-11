import os
import yaml
import pyodbc
import re

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
    global rows
    rows = []
    cursor = retornar_conexao_sql()
    cursor.execute(select)
    for row in cursor.fetchall():
        row = str(row)
        row = re.sub("[()']","",row)
        row = row.replace(', ', ',').replace(' ,',',')
        rows.append(row)
    return rows

def insert_sql(query,args):
    cursor = retornar_conexao_sql()
    cursor.execute(query,args)
    conexao.commit()
    print('gravado no banco')