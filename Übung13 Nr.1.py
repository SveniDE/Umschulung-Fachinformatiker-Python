def primetest(z):
    prime=True
    if z<=1:
        prime=False
        
    for i in range(2,int(z**0.5)+1):
        if z%i==0:
            prime=False
    produkt = 1

    for z in range(2, z + 1):
        prime=True

        for i in range(2, int(z**0.5) + 1):
            if z % i == 0:
                prime=False
                break

        if prime:
            produkt *= z
    return prime,produkt

print(primetest(1000))