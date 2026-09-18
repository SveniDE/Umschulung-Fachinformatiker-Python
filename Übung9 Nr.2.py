import statistics, math
liste=[77,32,1,98,55,3,8,7,22,13,8,44,72]

liste.sort()
print("")
print(liste)

liste.insert(0,0)
liste.append(99)
print(liste)

del liste[0]
del liste[-1]
liste.sort(reverse = True)
print(liste)

print("Die Summe ist: ", sum(liste))
print("Der Durchschnitt ist: ",statistics.mean(liste))
