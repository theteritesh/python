import sqlite3
conn=sqlite3.connect("Demo.db")
data=conn.execute("SELECT * FROM student")
for i in data:
    print(i)