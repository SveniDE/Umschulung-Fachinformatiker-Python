def addiere(a,b):  # "Eingabe"
    c = a + b      #  Verarbeitung
    return c       # "Ausgabe"
 
def countdown(n):   # Beispiel für rekursive Funktionen
    if n>=0:
        print(n)
        countdown(n-1)  # Rekursiver Aufruf
 
def countup(n):   # Beispiel für rekursive Funktionen
    if n>=0:
        countup(n-1)  # Rekursiver Aufruf
        print(n)      # print erfolgt erst beim Ende der Rekursion
 
 
#Main
print(addiere(1.7, 5.4))
countup(10)