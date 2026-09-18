import sqlite3
db = sqlite3.connect("schule.db") # Erzeugt oder Öffnet eine Datenbankdatei und das Datenbankobjekt db
cursor = db.cursor() # Erzeugt ein Cursor-Objekt

sql = """CREATE TABLE schueler (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT NOT NULL, 
    alterj INTEGER, 
    klasse TEXT)"""
cursor.execute(sql)  # SQL ausführen

db.close()  # DB geschlossen
print("Datenbank und Tabelle angelegt!")
