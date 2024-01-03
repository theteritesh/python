import sqlite3
conn=sqlite3.connect("Demo.db")
id=int(input("Enter The ID"))
data=conn.execute("SELECT * FROM student WHERE sid="+str(id)+"")
for i in data:
    print(i)