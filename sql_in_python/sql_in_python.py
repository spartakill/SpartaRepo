import pyodbc
import pandas as pd
import sqlalchemy

#print(pyodbc.drivers())

server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'yourStrong(!)Password'
driver = 'ODBC Driver 17 for SQL Server'

pyodbc_conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
sqlalchemy_conn = sqlalchemy.create_engine(f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}")
cursor = pyodbc_conn.cursor()

# print(cursor.execute("SELECT @@version;"))
# row = cursor.fetchone()
# print(row)

cust_rows = cursor.execute("SELECT * FROM Customers;").fetchall()
#print(cust_rows)

cust_rows_obj = cursor.execute("SELECT * FROM Customers;")
customers_df = pd.DataFrame(cust_rows_obj)
#print(customers_df)

sql_query = 'SELECT * FROM Customers'
df = pd.read_sql(sql_query, sqlalchemy_conn)
#print(df)

# creating the DataFrame
paris_cus_df = pd.read_sql("SELECT * FROM Customers WHERE city = 'Paris'",con=sqlalchemy_conn)
#print(paris_cus_df)

# using to_sql to create a table from the DataFrame
paris_cus_df.to_sql(name="paris_customers", con=sqlalchemy_conn, if_exists="replace")

# checking everything worked by querying the new table
query = pd.read_sql_query("SELECT * FROM paris_customers;", con=sqlalchemy_conn)
#print(query)