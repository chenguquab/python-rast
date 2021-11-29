from pathlib import Path
import json
import sqlite3


data = Path("data.json").read_text()
words_list = json.loads(data)

with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    command_create_table = """
    CREATE TABLE if NOT EXISTS "Dictionary" (
	"id"	INTEGER,
	"word"	TEXT,
	"meaning"	TEXT,
	PRIMARY KEY("id")
    );
    """
    cursor.execute(command_create_table)
    command = "INSERT INTO Dictionary (word, meaning) VALUES (?,?)"
    for word in words_list:
        meanings = words_list[word]
        for meaning in meanings:
            cursor.execute(command, (word, meaning))


    conn.commit()
