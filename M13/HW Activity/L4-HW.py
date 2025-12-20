import sqlite3
import pandas as pd

conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

conn.execute('''CREATE TABLE CLASS_09
(SNO INT PRIMARY KEY NOT NULL,
Roll_No INT NOT NULL,
Name TEXT NOT NULL,
AGE INT DEFAULT 15,
Contact_No REAL NOT NULL);''')

print("Table created successfully")

conn.execute("""INSERT INTO CLASS_09 (SNO, ROll_No, NAME, AGE, Contact_No)
                VALUES(1, 1, 'Debangana', 15, 7596984);""")

conn.execute("""INSERT INTO CLASS_09 (SNO, ROll_No, NAME, AGE, Contact_No)
                VALUES(2, 2, 'Shreeja', 14, 8240200);""")

conn.execute("""INSERT INTO CLASS_09 (SNO, ROll_No, NAME, AGE, Contact_No)
                VALUES(3, 3, 'Adwaitaa', 14, 6290351);""")

conn.commit()
print("Records created successfully")

class_09d = pd.read_sql("""SELECT *
                           FROM CLASS_09;""", conn)

print(class_09d.head())

