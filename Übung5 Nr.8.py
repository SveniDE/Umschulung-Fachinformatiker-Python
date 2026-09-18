summe = 0
anzahl = int(input("Anzahl Durchläufe>"))

for z in range(1,anzahl+1):
    summe = summe + z
    print(summe)
    print("Mittelwert: ",summe/anzahl)

print("Ende")

