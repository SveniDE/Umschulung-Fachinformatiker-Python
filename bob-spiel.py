import random

gewinn_ich=0
gewinn_bob=0

for z in range(100000):
    summe = 0
    for i in range(10):
        summe = summe + random.randint(1,6)

    if summe >= 40 and summe <= 50:
        gewinn_ich = gewinn_ich + 10
    else:
        gewinn_bob = gewinn_bob + 2


print(f"Ich: {gewinn_ich:8}")
print(f"Bob: {gewinn_bob:8}")