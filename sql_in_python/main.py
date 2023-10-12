import pyodbc
import sqlalchemy
import pandas as pd


print(pyodbc.drivers())

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'yourStrong(!)Password'
driver = 'ODBC Driver 17 for SQL Server'

pyodbc_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
sqlalchemy_conn = sqlalchemy.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
cursor = pyodbc_conn.cursor()