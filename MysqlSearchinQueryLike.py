import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
print("{:<15} {:<20} {:<20} {:<10}".format("Student ID","Student Name","Student Class","Student Email"))

try:
    name=input("Enter name whose You want Display The data =")
    curs.execute("SELECT *FROM student WHERE st_name like '%"+name+"%'")
    data= curs.fetchall()
    for i in data:
        print("{:<15} {:<20} {:<20} {:<10}".format(i[0],i[1],i[2],i[3]))

except:
    print("ERROR....")

finally:
    conn.close()