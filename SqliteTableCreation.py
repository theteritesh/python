import sqlite3
conn=sqlite3.connect("Demo.db")

str="""
    CREATE TABLE student (
    sid INTEGER PRIMARY KEY AUTOINCREMENT,
    sname VARCHAR(20),
    dipart VARCHAR(10)
    )
"""

conn.execute(str)
conn.commit()
conn.close()