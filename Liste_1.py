print("-"*30)
liste1=["Hans","Meier",True, 750.99]
liste2=[5,7,8,1,2,44,9,23,44,77]
liste3=[]
liste4=[["Hans","Maier"] , ["Erna" , "Schulz"]]   #Liste in Liste ist auch machbar

liste2.append(100)  # hänngt die Zahl 100 an die bestehende Liste2 an
print(liste2)       # gibt die ganze liste2 aus
print(liste2[0])    # Nur das ELement 0
print(liste2[0:2])  #gibt die ELemente 0 bis 2 aus der Liste 2 aus
print(liste2[-1])   # gibt das letzte Element der Liste2 aus
liste2[-1]=101      # ändert das letzte Element der Liste2 von 100 zu 101
print(liste2)
liste2.insert(0,0)  #fügt bei Liste2 an erster stelle eine 0 ein
print(liste2)
del liste2[3]       #element 3 (eine 8) löschen
print(liste2)
liste2.sort()       #sortiert Liste 2 aufsteigend
print(liste2)
liste2.sort(reverse=True)   #sortiert die Liste absteigend
print(liste2)
liste4.sort()       #liste in Liste sortiert
print(liste4)

for e in liste2:
    print(e,end=" ")

print("\n","-"*30)