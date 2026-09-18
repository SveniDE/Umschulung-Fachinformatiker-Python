while True:

    j = int(input("Jahreszahl eingeben > "))

    if j % 400 == 0:
        print("Es ist ein Schaltjahr")
    elif j % 100 == 0:
        print("Es ist kein Schaltjahr")
    elif j % 4 == 0:
        print("Es ist ein Schaltjahr")
    else:
        print("Es ist kein Schaltjahr")

    weiter = input("Erneut prüfen? (j/n) > ").lower()

    if weiter != "j":
        break

print("Programm beendet.")
