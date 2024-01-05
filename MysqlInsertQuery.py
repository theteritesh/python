import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
try:
    ins="INSERT INTO student(st_name,st_class,st_email) VALUES(%s,%s,%s)"
    name=input("Enter Name = ")
    cls=input("Enter a class name = ")
    eml=input("Enter Email ID = ")
    data=(name,cls,eml)
    curs.execute(ins,data)
    conn.commit()
    print("DATA INSERTED SUCSESSFULLY.....")
except :
    print("ERROR OCCURE WHILE INSERTING DATA INTO TABLE")
finally:
    conn.close()