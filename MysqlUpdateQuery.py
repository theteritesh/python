import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
id=int(input("Entr ID of STUDENT whose you want Update Data = "))
name=input("Enter new name = ")
cls=input("Enter new Class =")
email=input("Enter new Email = ")
data=(name,cls,email,id)
sql="UPDATE student SET st_name=%s,st_class=%s,st_email=%s WHERE s_id=%s"
try:
    curs.execute(sql,data)
    conn.commit()
except Exception:
    print(Exception)
finally:
    conn.close()