import pymysql as mq

conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
try:
    tb="CREATE TABLE student(s_id INT PRIMARY KEY AUTO_INCREMENT,st_name VARCHAR(50),st_class VARCHAR(10),st_email VARCHAR(30))"
    curs.execute(tb)
except:
    print("ERROR OCCURE WHILE CREATING TABLE...")
finally:
    conn.close()
    print("CONNECTION CLOSE....")