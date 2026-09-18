for j in range(2000,2031):
    if j % 400 == 0:
        print(j, "Es ist ein Schaltjahr")
    elif j % 100 == 0:
        print(j, "Es ist kein Schaltjahr")
    elif j % 4 == 0:
        print(j, "Es ist ein Schaltjahr")
    else:
        print(j, "Es ist kein Schaltjahr")

print("Ende")
