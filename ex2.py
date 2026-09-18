while True:
    try:
        e = int(input("Bitte eine ganze Zahl  > 0 eingeben> "))
        if e<=0: raise ValueError("Bitte>0")   # Einen Fehler auslösen
        break   # Schleife abbrechen, wenn Eingabe keinen Fehler hat
    except Exception as fehler:
        print("Bitte keinen Blödsinn eingeben!", fehler)

print(e)
