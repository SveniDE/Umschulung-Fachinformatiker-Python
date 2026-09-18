#liste gefüllt mit Zufallszahlen
import random                   #imortieren des random moduls

# generiert eine Liste mit 100 einträgen mit zufälligen zahlen zwischen 1 und 1000
liste=[]
for i in range(100):
    z = random.randint(1,1000)
    liste.append(z)


print(liste)
