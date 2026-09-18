import mysql.connector


db = mysql.connector.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Start-66780",
                             database = "world")

cursor=db.cursor()

# Aufgabe a
sql = "SELECT Name, LifeExpectancy FROM country ORDER BY LifeExpectancy DESC LIMIT 10"
cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]:15} {ds[1]:5.1f}")
print()

# Aufgabe b
sql = "SELECT Name, Population FROM city ORDER BY Population DESC LIMIT 10"
cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]:20} {ds[1]:10}")
print()

# Aufgabe c
sql = "SELECT Name, GNP, GovernmentForm FROM country ORDER BY gnp DESC LIMIT 10"
cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]:15} {ds[1]:8.0f} {ds[2]}")
print()

# Aufgabe d
sql = "SELECT Name, Population/SurfaceArea AS PopDensity FROM country ORDER BY PopDensity DESC LIMIT 5"
cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]:15} {ds[1]:8.2f}")
print()

# Aufgabe e
print("Aufgabe e")
# Lösung mit SubQuery
sql="""SELECT Name, cl.Language
    FROM (SELECT Code, Name, Population FROM country ORDER BY Population DESC LIMIT 5) AS c
    JOIN countrylanguage cl ON c.Code = cl.CountryCode"""

cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]:15} {ds[1]:12}")
print()

# Aufgabe f
print("Aufgabe f")
sql = """SELECT AVG(Population) FROM (SELECT * FROM country WHERE LifeExpectancy IS NOT NULL 
        ORDER BY LifeExpectancy ASC LIMIT 5 ) AS L"""
cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]}")
print()

# Aufgabe g
print("Aufgabe g")
sql = """SELECT AVG(Population) FROM (SELECT * FROM country WHERE LifeExpectancy IS NOT NULL 
        ORDER BY LifeExpectancy DESC LIMIT 5 ) AS L"""
cursor.execute(sql)
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]}")
print()

land = input("Land>")
sql = """SELECT c.Name, c.Population FROM city as c
        JOIN country co ON c.CountryCode = co.code
        WHERE co.Name = %s ORDER BY c.Population DESC"""

# Statt ? den Platzhalter %s verwenden beim mysql.connector

cursor.execute(sql,[land])
liste=cursor.fetchall()
for ds in liste:
    print (f"{ds[0]} {ds[1]}")
print()
db.close()

 