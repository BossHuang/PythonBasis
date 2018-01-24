__author__ = 'leihuang'

import sqlite3

DATAS = [["Tom",100],["Jack",99]]

conn = sqlite3.connect("databaseDemo.db")
curs = conn.cursor()

curs.execute('''
create table demo(
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 name varchar(10),
 score double
)
''')

query = 'insert into demo VALUES (?, ?,?)'

for data in DATAS:
    values = [None]
    values += data
    print values
    curs.execute(query, values)

conn.commit()
conn.close()
