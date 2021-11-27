import json
from pathlib import Path
from difflib import get_close_matches
import sqlite3

q = input("What?? ")
with sqlite3.connect("dic.db") as conn:
    cursor = conn.cursor()
    all_cursor = conn.cursor()
    all_command = "SELECT word FROM words_table"
    all_cursor.execute(all_command,)
    words = []
    for row in all_cursor:
        words.append(row[0])
    command = "SELECT * FROM words_table WHERE word = ? "
    cursor.execute(command, (q,))
    data = cursor.fetchall()
    if len(data)==0:
        close = get_close_matches(q, words)
        print('Did You mean, ', close[0], '?')
        ans = input('y/n :')
        if ans == 'y':
            cursor.execute(command, (close[0],))
            for row in cursor:
                print(row[2])
    else:
        print('FOUND')
        cursor.execute(command, (q,))
    for row in cursor:
        print(row[2])













# cc=0
# for word in words:
#     print(cc, word, words[word])
#     cc+=1
# with sqlite3.connect("dic.db") as conn:
#     cursor = conn.cursor()
#     command = "INSERT INTO words_table VALUES(?,?,?)"
#     cc = 0
#     for word in words:
#         cursor.execute(command, (cc, word, str(words[word])))
#         cc += 1
#     conn.commit()

