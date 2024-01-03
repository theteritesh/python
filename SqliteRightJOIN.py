import sqlite3

conn = sqlite3.connect("Demo.db")
str="SELECT s.sid,s.sname,f.fees FROM student as s RIGHT JOIN fees as f ON s.sid=f.sid"
data =conn.execute(str)
for i in data:
    print(i)