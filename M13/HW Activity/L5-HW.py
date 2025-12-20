import sqlite3

def get_joined_data(query_type):
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE Products (prod_id INTEGER PRIMARY KEY, prod_name TEXT, user_fav INTEGER)")
    cursor.execute("INSERT INTO Users VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie')")
    cursor.execute("INSERT INTO Products VALUES (101, 'Laptop', 1), (102, 'Mouse', 1), (103, 'Keyboard', 3), (104, 'Monitor', 4)")
    conn.commit()

    queries = {
        'INNER': "SELECT U.name, P.prod_name FROM Users U INNER JOIN Products P ON U.id = P.user_fav",
        'LEFT': "SELECT U.name, P.prod_name FROM Users U LEFT JOIN Products P ON U.id = P.user_fav"
    }
    
    sql_query = queries.get(query_type.upper())

    cursor.execute(sql_query)

    results = cursor.fetchall()
    for row in results:
        print(row)

    conn.close()