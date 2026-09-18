import random

ratezahl = random.randint(0,99)
gefunden = False

while True:
    if gefunden == True:
        break

    while gefunden == False:
        vorschlag=int(input("Deine Zahl: "))
        if vorschlag < ratezahl:
            print("Zu klein!")
        elif vorschlag > ratezahl:
            print("Zu groß!")
        elif vorschlag == ratezahl:
            print("Treffer!")
            gefunden =True

