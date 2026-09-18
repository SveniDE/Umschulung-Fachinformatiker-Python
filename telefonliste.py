import sqlite3, os

def db_anlegen():
    e= input("Sind Sie sicher? (j/n)>")
    if e!= "j":return
    
    try:
        os.remove("telefon.db")
    except:
        print("DB war nicht vorhanden")
    
    db = sqlite3.connect("telefon.db")
    cursor = db.cursor()
    sql = """CREATE TABLE telefon (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            Telefonnummer TEXT)"""
    cursor.execute(sql)
    print("DB angelegt")
    db.close()

def tel_einfuegen():
    db = sqlite3.connect("telefon.db")
    cursor = db.cursor()
    while True:
        n = input("Name>")
        if n=="": break
        t = input("Telefonnummer>")
        sql = "INSERT INTO telefon (Name, Telefonnummer) VALUES (?,?)"
        cursor.execute(sql,[n,t])
        db.commit()
    db.close()

def tel_ausgabe():
    db = sqlite3.connect("telefon.db")
    cursor = db.cursor()
    sql = "SELECT * FROM telefon ORDER BY Name"
    cursor.execute(sql)

    liste = cursor.fetchall()  # Alle Daten aus dem Cursor in eine Liste transferieren
    
    db.close()
    print()
    print(" ID Name                      Telefonnummer")
    print("-------------------------------------------")
    for ds in liste:
        print(f"{ds[0]:3} {ds[1]:25} {ds[2]}")

def tel_löschen():
    tel_ausgabe()
    id = input("Welche ID soll gelöscht werden>")
    db = sqlite3.connect("telefon.db")
    cursor = db.cursor()
    sql = "DELETE FROM telefon WHERE ID=?"
    cursor.execute(sql,[id])
    db.commit()
    db.close()

def main():
    while True:
        print("\nHauptmenü Telefon Datenbank")
        print("1. DB löschen und neu anlegen")
        print("2. Telefonnummer erfassen")
        print("3. Telefonliste ausgeben (nach Namen)")
        print("4. Telefonnummer löschen")
        print("9. Ende")
        e = input("Menüpunkt>")
        if e=="9":break
        elif e=="1": db_anlegen()
        elif e=="2": tel_einfuegen()
        elif e=="3": tel_ausgabe()
        elif e=="4": tel_löschen()

main()