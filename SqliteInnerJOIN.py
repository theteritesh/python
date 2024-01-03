import sqlite3

conn = sqlite3.connect("Demo.db")
str="SELECT s.sid,s.sname,f.fees FROM fees as f INNER JOIN student as s ON s.sid=f.sid"
data =conn.execute(str)
for i in data:
    print(i)