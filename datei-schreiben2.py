import time

e = input("Name> ")
do = open("test2.txt","a",encoding="utf-8") # Datei öffnen zum Anhängen(a=append)
do.write(time.ctime())  # Aktuelle Uhrzeit schreiben
do.write(" - Benutzername:" +e+"\n")    # Benutzereingabe schreiben
do.close()  # Datei schließen
print("Uhrzeit in Datei geschrieben")