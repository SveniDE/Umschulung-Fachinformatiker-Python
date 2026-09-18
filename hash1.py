def hash(eingabe):
    summe = 0
    # 8-Bit-Hashwert
    for b in eingabe:
        code = ord(b)
        summe = summe + code

    hash = summe % (256)    # 256 = 2^8 Bit
    return hash

while(True):
    eingabe = input("Eingabetext> ")
    
    print(f"{hash(eingabe):2x}")

