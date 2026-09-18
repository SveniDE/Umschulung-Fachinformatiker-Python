import time,random
liste=[5,2,-3,4,1]
rliste=[]

for i in range(5000):
    x = random.randint(1,100000)
    rliste.append(x)

z1 = time.time()
for n in range (len(rliste),1,-1):
    for i in range (0,n-1):
        if rliste[i] > rliste[i+1]:
            tausch = rliste[i]
            rliste[i] = rliste[i+1]
            rliste[i+1] = tausch

z2 = time.time()
#print(rliste)
print("der Bubblesort hat ", z2-z1, "Sekunden gedauert")
# 5000- 8,50s
# 10000- 34,34s
# 20000- 119,51s