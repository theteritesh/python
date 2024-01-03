import sqlite3
conn=sqlite3.connect("Demo.db")
str="DELETE FROM student WHERE sname='Dinesh'"
str1="DELETE FROM student WHERE sname='Ganesh'"

conn.execute(str)
conn.execute(str1)
conn.commit()
conn.close()