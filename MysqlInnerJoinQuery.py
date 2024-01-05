import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
print("{:<15} {:<20} {:<20} {:<10}".format("Student ID","Student Name","Employee Dipartment","Employee Email"))

try:
    curs.execute("SELECT *FROM student INNER JOIN employee ON student.st_name=employee.st_name ")
    data= curs.fetchall()
    for i in data:
        
        print("{:<15} {:<20} {:<20} {:<10}".format(i[0],i[1],i[6],i[7]))

except:
    print("ERROR....")

finally: 
    conn.close()