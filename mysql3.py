import mysql.connector

db = mysql.connector.connect(host="cloud.rothnet.org", 
                            port = 3336,
                            user = "fachi",
                            password= "fachi2025",
                            database = "Northwind")

cursor = db.cursor()
sql = """SELECT o.city, e.employeeNumber, e.firstName, e.lastName, e.jobTitle FROM offices o
        JOIN employees e
            ON o.officeCode = e.officeCode
            ORDER BY o.officeCode, e.lastName"""


cursor.execute(sql)

for ds in cursor:
    print(ds)
db.close()




