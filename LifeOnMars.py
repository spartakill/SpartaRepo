import requests
import json
import pandas as pd
from sqlalchemy import create_engine
import pyodbc

url = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+pl_name,disc_year,pl_controv_flag,pl_orbper,pl_orbsmax,pl_rade,pl_bmasse,pl_orbeccen,pl_eqt,sy_dist+from+pscomppars&format=json"

response = requests.get(url)

print(response)

data = response.json()

df = pd.DataFrame(data)

server_name = 'localhost,1433'
database_name = 'LifeOnMars'
username = 'SA'
password = 'yourStrong(!)Password'

# Example connection string for SQL Server
connection_string = f'DRIVER=ODBC Driver 17 for SQL Server;SERVER={server_name};DATABASE=master;UID={username};PWD={password}'

try:
    conn = pyodbc.connect(connection_string, autocommit=True)
except pyodbc.Error as e:
    print(f"Error connecting to SQL Server: {e}")
    exit()

cursor = conn.cursor()

drop_exoplanets_sql = """
DROP TABLE IF EXISTS exoplanets
"""

create_exoplanets_sql = """
CREATE TABLE exoplanets (
    pl_name VARCHAR(50),
    disc_year INT,
    pl_controv_flag INT,
    pl_orbper INT,
    pl_orbsmax INT,
    pl_rade INT,
    pl_bmasse INT,
    pl_orbeccen INT,
    pl_eqt INT,
    sy_dist INT
)
"""

try:
    cursor.execute(drop_exoplanets_sql)
    cursor.execute(create_exoplanets_sql)
    print("Exoplanets table created successfully.")
except pyodbc.Error as e:
    print(f"Error creating tables: {e}")

cursor.close()
conn.close()

server_name = 'localhost,1433'
database_name = 'LifeOnMars'
username = 'SA'
password = 'yourStrong(!)Password'

# Example connection string for SQL Server
connection_string = f'mssql+pyodbc://{username}:{password}@{server_name}/{database_name}?driver=ODBC+Driver+17+for+SQL+Server'
engine = create_engine(connection_string)

# Assuming df is your DataFrame
df.to_sql(name='exoplanets', con=engine, if_exists='replace', index=False)

# Dispose of the engine when done
engine.dispose()
