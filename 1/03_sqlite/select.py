import sqlite3

with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    command = "SELECT * FROM Movies"
    cursor.execute(command)
    for row in cursor:
        print(row)