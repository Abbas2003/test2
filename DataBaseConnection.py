import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Gotohell12345",
    database = "ihi_db"
)

cur = con.cursor()
cur.execute("select * from tbl_emp")
emp = cur.fetchall()
for i in emp:
    print(i)

cur.close()
con.close()