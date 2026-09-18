#fakultät berechnene

for n in range(5,10):
    fak=1
    for i in range(1,n+1):
        fak=fak*i
    print(f"Die Fakultät von {n} ist {fak}")