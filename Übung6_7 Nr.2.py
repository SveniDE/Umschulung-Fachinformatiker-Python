z = int(input(">"))
prim=True

if z<=1:
    print(z, "ist keine Primzahl")
else:
    for i in range(2,z):
        if z % i == 0 or z == 1:
            prim=False
            print(z, "ist keine Primzahl")
            break
    else:
        print(z, "ist eine Primzahl")
