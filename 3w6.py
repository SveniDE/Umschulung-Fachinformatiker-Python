import random as r
r.seed(100)
samples = 500000
z = 0

for i in range(samples):
    if r.randint(1,6) == 6 and r.randint(1,6) == 6 and r.randint(1,6) == 6:
        z += 1

print(z/samples*100, "%")