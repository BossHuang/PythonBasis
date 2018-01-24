__author__ = 'leihuang'

import sqlite3
conn = sqlite3.connect("databaseDemo.db")
curs = conn.cursor()

query = 'select * from demo'
curs.execute(query)
names = [d[0] for d in curs.description]
for row in curs.fetchall():
    print zip(names, row)