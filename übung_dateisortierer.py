def bubbleSort(liste):
    for n in range(len(liste),1,-1):
        for i in range(0,n-1):
            if liste[i]>liste[i+1]:
                liste[i],liste[i+1]=liste[i+1],liste[i]
    return liste

liste=[] 
datei=open("zahlen-unsortiert.txt","r")
for zeile in datei:
    liste.append(int(zeile))  # Einlesen in eine Liste und umwandeln in int
datei.close()

print(f"Anzahl:{len(liste)} - Mittelwert:{sum(liste)/len(liste):9.2f}") 

liste=bubbleSort(liste) # Liste sortieren  liste.sort()

liste=list(set(liste)) # Duplikate entfernen

print(f"Anzahl:{len(liste)} - Mittelwert:{sum(liste)/len(liste):9.2f}") 

datei=open("zahlen-sortiert.txt","w",encoding="utf-8")
for zeile in liste:
    datei.write(str(zeile)+"\n")
datei.close()
 