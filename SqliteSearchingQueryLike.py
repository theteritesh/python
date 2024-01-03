import sqlite3
conn=sqlite3.connect("Demo.db")
name=input("Enter The name =")
data=conn.execute("SELECT * FROM student WHERE sname like '%"+name+"%'")
for i in data:
    print(i)