import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
print("{:<15} {:<20} {:<20} {:<20} {:<10}".format("Student ID","Student Name","Emplyee Name","Employee Dipartment","Employee Email"))

# try:
curs.execute("SELECT *FROM student LEFT JOIN employee ON student.st_name=employee.st_name ")
data= curs.fetchall()
for i in data:
    
    print("{:<15} {:<20} {:<20} {:<20} {:<10}".format(str(i[0]),str(i[1]),str(i[5]),str(i[6]),str(i[7])))

# except:
#     print("ERROR....")

# finally: 
#     conn.close()