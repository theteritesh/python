import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='sup_shop')
curs=conn.cursor()
print("{:<20} ".format("Product Price"))

try:
    curs.execute("SELECT DISTINCT(category) FROM product ")
    data= curs.fetchall()
    for i in data:
        print("{:<20}".format(i[0]))

    
except:
    print("ERROR....")

finally:
    conn.close()