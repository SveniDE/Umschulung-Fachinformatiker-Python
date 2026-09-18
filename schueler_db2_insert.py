import sqlite3
db = sqlite3.connect("schule.db") # Erzeugt oder Öffnet eine Datenbankdatei und das Datenbankobjekt db
cursor = db.cursor() # Erzeugt ein Cursor-Objekt
sql = """INSERT INTO schueler (name, alterj, klasse)
    VALUES ('Annabella',27,'FI2027')"""
cursor.execute(sql)
sql = "INSERT INTO schueler (name, alterj, klasse) VALUES ('Hans',22,'FI2027')"
cursor.execute(sql)   # SQL ausführen
db.commit()  # Datentransfer bestätigen (Transaktion beenden)
print("Datensätze eingefügt")
db.close()
