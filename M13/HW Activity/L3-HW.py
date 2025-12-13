import sqlite3

conn = sqlite3.connect("db.sqlite")

conn.execute("""
CREATE TABLE IF NOT EXISTS Match (
    Match_ID INTEGER,
    Team1 TEXT,
    Team2 TEXT,
    Venue TEXT
)
""")

conn.execute("INSERT INTO Match VALUES (1,'India','Australia','Delhi',180,170)")
conn.execute("INSERT INTO Match VALUES (2,'India','England','Mumbai',220,200)")
conn.execute("INSERT INTO Match VALUES (3,'India','Pakistan','Delhi',140,130)")
conn.execute("INSERT INTO Match VALUES (4,'Australia','India','Mumbai',200,210)")

conn.commit()

print("Distinct Venues:")
for row in conn.execute("SELECT DISTINCT Venue FROM Match"):
    print(row)

print("\nMatches ordered by Team1 runs (DESC):")
for row in conn.execute("""
SELECT * FROM Match
ORDER BY Runs_Team1 DESC
"""):
    print(row)

print("\nNumber of matches played by each Team1:")
for row in conn.execute("""
SELECT Team1, COUNT(*)
FROM Match
GROUP BY Team1
"""):
    print(row)

print("\nAverage runs scored by each Team1:")
for row in conn.execute("""
SELECT Team1, AVG(Runs_Team1)
FROM Match
GROUP BY Team1
"""):
    print(row)