
do = open("test1.txt","w",encoding="utf_8")  # 1. Dateiobjekt erzeugen
do.write("Das ist meine erste Textdatei."+"\n")   # 2. In die Datei Text schreiben
do.write("Hier stehen Zahlen (0123456789) \noder Buchstaben äöüÄÖÜß\n")
do.write("Das Ergebnis von 10/5 ist: "+str(10/5))
do.close()  # 3. Dateionjekt schließen

print("****Datei geschlossen****")