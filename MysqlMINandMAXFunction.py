import pymysql as mq
conn=mq.connect(host='localhost',user='root',password='',database='sup_shop')
curs=conn.cursor()
print("{:<20}".format("Product Price"))

try:
    curs.execute("SELECT min(price) FROM product")
    data= curs.fetchall()
    for i in data:
        print("{:<20}".format(i[0]))

    curs.execute("SELECT max(price) FROM product")
    data1= curs.fetchall()
    for i in data1:
        print("{:<20}".format(i[0]))
except:
    print("ERROR....")

finally:
    conn.close()