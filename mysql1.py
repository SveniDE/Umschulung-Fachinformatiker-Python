import mysql.connector

db = mysql.connector.connect(host="cloud.rothnet.org", 
                            port = 3336,
                            user = "fachi",
                            password= "fachi2025",
                            database = "Northwind")

cursor = db.cursor()
sql = "SHOW TABLES"
cursor.execute(sql)

for ds in cursor:
    print(ds)
db.close()




