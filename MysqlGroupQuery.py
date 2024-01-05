import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='sup_shop')
curs=conn.cursor()
print("{:<20} {:<20}".format("Product Price","Count"))

try:
    curs.execute("SELECT category,COUNT(*) FROM product GROUP BY category")
    data= curs.fetchall()
    for i in data:
        print("{:<20} {:<20}".format(i[0],i[1]))

    
except:
    print("ERROR....")

finally:
    conn.close()