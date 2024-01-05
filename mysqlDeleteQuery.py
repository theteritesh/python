import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
id=int(input("Entr ID of STUDENT whose you want Delete Data = "))
try:
    sql="DELETE FROM student WHERE s_id=%s"
    curs.execute(sql,id)
    conn.commit()
    print("Data Is Deleted  Of Student ID =",id)
except:
    print("Something Went Wrong...")
finally:
    conn.close()