import sqlite3
conn = sqlite3.connect("konto.db")
cursor = conn.cursor()

sql = """
    CREATE TABLE konto ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    inhaber TEXT NOT NULL, 
    kontostand REAL NOT NULL DEFAULT 0.0);"""
cursor.execute(sql)

sql = """
    CREATE TABLE ueberweisung ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    quellkonto_id INTEGER NOT NULL, 
    zielkonto_id INTEGER NOT NULL, 
    betrag REAL NOT NULL CHECK (betrag > 0), 
    zeitstempel TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, 
 
    FOREIGN KEY (quellkonto_id) 
        REFERENCES konto(id), 
 
    FOREIGN KEY (zielkonto_id) 
        REFERENCES konto(id));"""
cursor.execute(sql)
conn.close()