import random

wuerfel1=[]

for i in range(1,1_000_000+1):
    z =random.randint(1,6)
    wuerfel1.append(z)
summe = sum(wuerfel1)
anzahl = len(wuerfel1)
print(summe)
print(anzahl)
mittel = sum(wuerfel1) / len(wuerfel1)
print(mittel)

for zahl in range(1,7):
    anzahleinzeln = wuerfel1.count(zahl)
    print(f"Zahl {zahl}: {anzahleinzeln} Mal")