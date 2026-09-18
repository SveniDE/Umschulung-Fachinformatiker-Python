def leistung(v,a):
    l=v*a
    return l

v=int(input("Volt>"))
a=int(input("Ampere>"))
print("Die Leistung von:",v,"Volt und",a,"Ampere ist:",leistung(v,a), "Watt")
