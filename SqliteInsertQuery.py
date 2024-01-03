import sqlite3

conn=sqlite3.connect("Demo.db")

str="INSERT INTO student(sname,dipart) VALUES ('Ritesh','MCA')"
str="INSERT INTO fees(sid,fees) VALUES (5,'20000')"

conn.execute(str)
conn.commit()
conn.close()