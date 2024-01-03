import sqlite3
conn=sqlite3.connect("Demo.db")
str="""
    UPDATE student SET sname='Mahesh' WHERE sid=2
"""
conn.execute(str)
conn.commit()
conn.close()