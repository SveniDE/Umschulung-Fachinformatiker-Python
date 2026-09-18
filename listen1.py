# Listenerstellung
liste1=["Hans","Meier",True,750.99]
liste2=[5,7,8,1,2,44,9,23,44,77]
liste3=[]
liste4=[["Hans","Meier"] , ["Erna","Schulze"]]

liste2.append(100)  # An Liste anhängen
liste2.extend([200,300])
print(liste2)       # Komplette Liste
print(liste2[0])    # Nur das Element 0 (Das erste in der Liste)
print(liste2[1:3])  # Einen Teil der Liste ausgeben (Element 1 und 2)
print(liste2[-1])   # Letztes Element
liste2[-1]=101      # Letztes Element (300) auf 101 setzen
print(liste2)
liste2.insert(0,0)  # An erster Stelle eine 0 einfügen
print(liste2)
del liste2[3]       # Element 3 (eine 8) löschen
print(liste2)
liste2.sort()       # Listenelemente aufsteigend sortieren
print(liste2)
liste2.sort(reverse=True)       # Listenelemente absteigend sortieren
print(liste2)
liste4.sort()       # Liste in Liste aufsteigend sortieren
print(liste4)

for e in liste2:    # Durch eine Liste "durchinterieren" (mit Schleife for durchlaufen)
    print(e,end=" ")
print("\nDie Liste2 hat",len(liste2),"Elemente")
