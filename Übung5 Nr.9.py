summe = 0

for z in range(1,1000):
    if z % 3 == 0 or z % 5 == 0:
        print(z)
        summe = summe + z
print("Summe aller Zahlen: ",summe)

print("Ende")

