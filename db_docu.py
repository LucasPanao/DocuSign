import os
import yaml
import pyodbc

with open('config.yml') as f:
    db_config = yaml.safe_load(f)
server = db_config['db-config']['server']
database = db_config['db-config']['database']
username = db_config['db-config']['username']
password = db_config['db-config']['password']
valor_id = '123453999'
valor_id2 = '231365'

def retornar_conexao_sql():
    global conexao
    string_conexao = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()

def select_sql(select):
    cursor = retornar_conexao_sql()
    cursor.execute(select)
    row = cursor.fetchone()
    if row:
        print(row)

def insert_sql(query,args):
    cursor = retornar_conexao_sql()
    cursor.execute(query,args)
    conexao.commit()
    print("gravado no banco")

                  