import time
t1 = time.time()   # Aktuelle Uhrzeit in Sekunden seit Epoch
print("Sekunden nach Epoch",t1)
print("Datum/Uhrzeit:",time.ctime(t1)) # Umwandlung Epoch in Kalenderzeit/datum
time.sleep(5)  # Wartezeit in sekunden
print("Datum/Uhrzeit:",time.ctime()) # Umwandlung Aktuelle Zeit in Kalenderzeit/datum

zeitstruktur = time.localtime() # Erzeugt ein Zeitobjekt, welches man später bei der Ausgabe formtieren kann
print(zeitstruktur)