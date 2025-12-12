#Import necessary libraries
import pandas as pd
import sqlite3

#Name of your SQLite database file
database = "database.sqlite"

#Connect to the database
conn = sqlite3.connect(database)
print("Opened database successfully")

#Get list of all tables
tables = pd.read_sql(""" SELECT name
                        FROM sqlite_master
                        WHERE type='table';""", conn)
                        
print("All Tables in the Database:")
print(tables)

#Load the 'Team' table
teams = pd.read_sql("""SELECT * FROM Team;""", conn)

print("\nTeam Table (first 5 rows):")
print(teams.head())

#Load the 'Match' table
matches = pd.read_sql("""SELECT * FROM Match;""", conn)

print("\nMatch Table (first 5 rows):")
print(matches.head())

#Check details of all matches won by Mumbai Indians
#    (Assuming Mumbai Indians has Team_Id = 7)
MI_wins = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7;""", conn)

print("\n---All MI Wins---")
print(MI_wins)

#Matches won by MI in last two seasons 
#     (Assuming seasons 8 and 9)
MI_S8_S9 = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7 AND Season_Id IN (8,9)""")