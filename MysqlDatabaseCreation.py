import pymysql 
conn=pymysql.connect(host="localhost",user="root",password="")
curs=conn.cursor()

try:
    db="CREATE DATABASE school"
    curs.execute(db)


except:
    print("Error Ocuured WHile DATABASE creating.......")