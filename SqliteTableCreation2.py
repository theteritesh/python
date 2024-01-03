import sqlite3
conn=sqlite3.connect("Demo.db")

str="""
    CREATE TABLE fees(
    fid INTEGER PRIMARY KEY AUTOINCREMENT,
    sid INTEGER,
    fees VARCHAR(10)
    )
"""

conn.execute(str)
conn.commit()
conn.close()