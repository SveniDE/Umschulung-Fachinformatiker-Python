import sqlite3, os

def db_anlegen():
    e= input("Sind Sie sicher? (j/n)>")
    if e!= "j":return
    
    try:
        os.remove("bank.db")
    except:
        print("DB war nicht vorhanden")
    
    db = sqlite3.connect("bank.db")
    cursor = db.cursor()
    sql = """CREATE TABLE konto (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            inhaber TEXT NOT NULL,
            kontostand REAL NOT NULL DEFAULT 0)"""
    cursor.execute(sql)
    sql = """CREATE TABLE ueberweisung (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quellkonto_id INTEGER NOT NULL,
            zielkonto_id INTEGER NOT NULL,
            betrag REAL NOT NULL CHECK (betrag > 0),
            zeitstempel TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (quellkonto_id)
                REFERENCES konto(id)
            FOREIGN KEY (zielkonto_id)
                REFERENCES konto(id))"""
    cursor.execute(sql)
    print("DB angelegt")
    db.close()

def konto_anlegen():
    db = sqlite3.connect("bank.db")
    cursor = db.cursor()
    while True:
        n = input("Inhaber> ")
        if n=="": break
        k = input("Kontostand> ")
        sql = "INSERT INTO konto (inhaber, kontostand) VALUES (?,?)"
        cursor.execute(sql,[n,k])
        db.commit()
    db.close()

def ueberweisung_hinzufügen():
    db = sqlite3.connect("bank.db")
    cursor = db.cursor()
    while True:
        q = input("Von welchem Inhaber> ")
        if q=="": break
        z = input("Zu welchem Inhaber> ")
        b = input("Wie viel?> ")
        sql = "INSERT INTO ueberweisung (quellkonto_id, zielkonto_id, betrag) VALUES (?,?,?)"
        cursor.execute(sql,[q,z,b])
        db.commit()
    db.close()

def ueberweisung_ausgabe():
    db = sqlite3.connect("bank.db")
    cursor = db.cursor()
    sql = "SELECT * FROM ueberweisung ORDER BY quellkonto_id"
    cursor.execute(sql)

    liste = cursor.fetchall()  # Alle Daten aus dem Cursor in eine Liste transferieren
    
    db.close()
    print()
    print(" ID       von       an                     betrag")
    print("-------------------------------------------------")
    for ds in liste:
        print(f"{ds[0]:3}     {ds[1]:13} {ds[2]:13} {ds[3]:6}")

def konto_ausgabe():
    db = sqlite3.connect("bank.db")
    cursor = db.cursor()
    sql = "SELECT * FROM konto ORDER BY inhaber"
    cursor.execute(sql)

    liste = cursor.fetchall()  # Alle Daten aus dem Cursor in eine Liste transferieren
    
    db.close()
    print()
    print(" ID   inhaber                betrag")
    print("-----------------------------------")
    for ds in liste:
        print(f"{ds[0]:3} {ds[1]:25} {ds[2]}")

def main():
    while True:
        print("\nHauptmenü Telefon Datenbank")
        print("1. DB löschen und neu anlegen")
        print("2. Konto hinzufügen")
        print("3. Überweisung hinzufügen")
        print("4. Überweisungen anzeigen")
        print("5. Konten anzeigen")
        print("9. Ende")
        e = input("Menüpunkt>")
        if e=="9":break
        elif e=="1": db_anlegen()
        elif e=="2": konto_anlegen()
        elif e=="3": ueberweisung_hinzufügen()
        elif e=="4": ueberweisung_ausgabe()
        elif e=="5": konto_ausgabe()

main()