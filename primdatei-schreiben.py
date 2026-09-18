def primtest(z):
    prim=True
    for i in range(2, int((z**0.5))+1):
        if z%i==0:
            prim=False
            return prim
    if z==1: prim=False
    return prim

do = open("primzahlen.txt","w",encoding="utf-8")
for i in range(2,1_000_001):
    if primtest(i):
        do.write(str(i)+ "\n")
do.close()
print("Primzahl geschrieben")