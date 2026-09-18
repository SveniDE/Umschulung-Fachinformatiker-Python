while True:
    z = int(input("Zahl, 0 zum Abbruch>"))
    if z==0: break
    prim = True
    if z<=1: prim=False
    for i in range(2,z):
        if z%i==0:
            prim=False
            break
    print(prim)

print("*** Ende ***")
 
