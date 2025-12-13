import sqlite3

conn = sqlite3.connect("db.sqlite")

conn.execute("""
CREATE TABLE IF NOT EXISTS Match (
    Match_ID INTEGER,
    Team1 TEXT,
    Team2 TEXT,
    Venue TEXT,
    Runs_Team1 INTEGER,
    Runs_Team2 INTEGER
)
""")

conn.execute("INSERT INTO Match VALUES (1,'India','Australia','Delhi',180,170)")
conn.execute("INSERT INTO Match VALUES (2,'India','England','Mumbai',220,200)")
conn.execute("INSERT INTO Match VALUES (3,'India','Pakistan','Delhi',140,130)")

conn.commit()

print("All Records:")
for row in conn.execute("SELECT * FROM Match"):
    print(row)

print("\nMatches played at Delhi:")
for row in conn.execute("SELECT * FROM Match WHERE Venue = 'Delhi'"):
    print(row)

print("\nMatches where Team1 scored more than 150:")
for row in conn.execute("SELECT * FROM Match WHERE Runs_Team1 > 150"):
    print(row)
