import sqlite3
db = sqlite3.connect("schule.db") # Erzeugt oder Öffnet eine Datenbankdatei und das Datenbankobjekt db
cursor = db.cursor() # Erzeugt ein Cursor-Objekt
sql = "SELECT * FROM schueler WHERE id<5 ORDER BY id"
cursor.execute(sql)
for ds in cursor:
    print(f"{ds[0]:2} {ds[1]:16} {ds[2]:3} {ds[3]:8}")
db.close()