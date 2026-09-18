import statistics, random

while True:
    n = int(input("Zahl eingeben(0 für Beenden)>"))
    qs=0

    if n <= 0:
        break

    while n>0:
        qs = qs + n % 10
        n = n // 10

    print("Quersumme:" , qs)
