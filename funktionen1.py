def doppel(x):
    e = x*2
    return e

def quadrat(x):
    return round(x**2,2)

def listenprodukt(liste):
    produkt = 1
    for e in liste:
        produkt=produkt*e
    return produkt

def begrüssung(n):      # Funktion OHNE return/Rückgabe --> Prozedur
    print("Hallo",n,"Du Nase!")

def info():
    print("******** Funktionsdemo V0.1 **********")

a=6.6
b=doppel(a)  # Funktionsauffruf mit Argument a
print(b)

print(quadrat(3.6789))

l1 = [2,3,5,6,7,9,10]
print(listenprodukt(l1))

name="Michael Roth"
begrüssung(name)

info()
 