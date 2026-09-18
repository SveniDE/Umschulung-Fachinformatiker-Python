import statistics, random
w =[]
for i in range(1_000_000):
    x = random.randint(1,6)
    w.append(x)

print(w)

print("Der Mittelwert ist", statistics.mean(w))


for i in range (1,7):
    print("Die",i,"ist",w.count(i),"mal vorgekommen")