import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
print("{:<15} {:<20} {:<20} {:<10}".format("Student ID","Student Name","Student Class","Student Email"))

try:
    curs.execute("SELECT *FROM student ORDER BY s_id ASC")
    data1= curs.fetchall()
    for i in data1:
        print("{:<15} {:<20} {:<20} {:<10}".format(i[0],i[1],i[2],i[3]))
    curs.execute("SELECT *FROM student ORDER BY s_id DESC")
    data2= curs.fetchall()
    print()
    print("{:<15} {:<20} {:<20} {:<10}".format("Student ID","Student Name","Student Class","Student Email"))
    for i in data2:
        print("{:<15} {:<20} {:<20} {:<10}".format(i[0],i[1],i[2],i[3]))

except:
    print("ERROR....")

finally:
    conn.close()