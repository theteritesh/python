import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
try:
    ins="INSERT INTO employee(st_name,e_dipart,e_email) VALUES(%s,%s,%s)"
    name=input("Enter Name = ")
    dip=input("Enter a Dipartment name = ")
    eml=input("Enter Email ID = ")
    data=(name,dip,eml)
    curs.execute(ins,data)
    conn.commit()
    print("DATA INSERTED SUCSESSFULLY.....")
except :
    print("ERROR OCCURE WHILE INSERTING DATA INTO TABLE")
finally:
    conn.close()