import sqlite3
db = sqlite3.connect("schule.db") # Erzeugt oder Öffnet eine Datenbankdatei und das Datenbankobjekt db
cursor = db.cursor() # Erzeugt ein Cursor-Objekt

while True:
    n=input("Name>")
    if n=="": break
    a=int(input("Alter>"))
    k=input("Klasse>")
    sql = "INSERT INTO schueler (name, alterj, klasse) VALUES (?,?,?)"  # Nur Platzhalter
    cursor.execute(sql,[n,a,k]) # Ausführen Platzhalter mit Variablen füllen gege SQL-Injection
    db.commit()
    print("Datensätze eingefügt")

db.close()
print("Programm beendet")