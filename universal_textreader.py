while True:
    dn = input("Dateiname> ")
    try:
        do = open(dn,"r")
        break
    except FileNotFoundError:
        print(dn, "gibts nicht")
for z in do:
    print(z,end="")
do.close()