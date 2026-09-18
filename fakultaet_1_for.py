#fakultät berechnene

#n = int(input("n:"))
for n in range(5,10):
    fakult =1
    for i in range(1, n+1):  
        fakult= fakult * i
    print(f"Die Fakultät von {n} ist {fakult}")


for n in range(5,10):
    fak=1
    for i in range(1,n+1):
        fak=fak*i
    print(f"Die Fakultät von {n} ist {fak}")