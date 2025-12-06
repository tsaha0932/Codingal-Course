import sqlite3
import pandas as pd

db_path = "database.sqlite"

conn = sqlite3.connect(db_path)

df = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table';", 
    conn
)

for table in df['name']:
    print(table)

conn.close()