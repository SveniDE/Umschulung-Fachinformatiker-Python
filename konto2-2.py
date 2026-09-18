import sqlite3
conn = sqlite3.connect("konto.db")
cursor = conn.cursor()

q = int(input("Quellkonto-ID>"))
z = int(input("Zielkonto-ID>"))
b = float(input("Betrag>"))

sql = "INSERT INTO ueberweisung (quellkonto_id, zielkonto_id, betrag) VALUES (?,?,?)"
cursor.execute(sql, [q,z,b])
conn.commit()

conn.close()