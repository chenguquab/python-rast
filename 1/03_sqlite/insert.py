import sqlite3

with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    command = "INSERT INTO Movies VALUES(?,?,?)"       
    cursor.execute(command, (2, 'ronin', 1991))
    conn.commit()