import random as r

zähler = 0
samples = 10
summe = 0
for z in range(samples):
    for i in range(2):
        summe = summe + r.randint(1,6)
    if summe >= 8:
        zähler += 1
print(zähler/samples*100,"%")

zähler9 = 0
zähler10 = 0
samples = 100

for i in range(samples):
        summe = 0
        for i in range(2):
            summe = summe + r.randint(1,6)
        if summe == 9:
            zähler9 += 1
        elif summe == 10:
            zähler10 += 1
             
print(f"Anzahl Würfe: {samples:5}   Anzahl 9: {zähler9:3}   Anzahl 10: {zähler10:3}  ")

import random as r
personen = 12
samples = 100000
mehrfach = 0

for _ in range(samples):
    geburtstage=365*[0]
    for i in range(personen):
        geburtstage[r.randrange(365)]+=1

    for i in geburtstage:
        if i>1 : 
            mehrfach = mehrfach +1   # Mehrfachgeburtstag gefunden!
            break                    # Wichtig damit nicht noch mehr Mehrfachgeburtstage gefunden werden

print("Mehrfachgeburtstagsquote:",mehrfach/samples*100)
 
