import math
def zukunftswert(betrag,jahre,jahreszins):
    endbetrag=betrag
    for i in range(1,jahre+1):
        endbetrag=endbetrag+(endbetrag*jahreszins/100)
    return endbetrag

print(round(zukunftswert(1000,15,4.95),2))