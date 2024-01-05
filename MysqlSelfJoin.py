import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='school')
curs=conn.cursor()
print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<10}".format("Student ID","Student Name","Another Student Name","Student Name","Student Email","Demo"))

try:


    curs.execute("SELECT * FROM employee as e1,employee as e2 WHERE e1.e_id=e2.demo")
    data= curs.fetchall()
    for i in data:
        
        print("{:<15} {:<20} {:<20} {:<20} {:<20} {:<10}".format(str(i[0]),str(i[1]),str(i[6]),str(i[2]),str(i[3]),str(i[4])))

except:
    print("ERROR....")

finally: 
    conn.close()