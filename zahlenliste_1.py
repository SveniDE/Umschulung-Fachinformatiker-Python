liste1=[77,32,1,98,55,3,8,7,22,13,8,44,72]

liste1.sort()
print(liste1)
liste1.insert(0,0)
print(liste1)
liste1.append(99)
print(liste1)
del liste1[0]
print(liste1)
del liste1[-1]
print(liste1)
liste1.sort(reverse=True)
print(liste1)
Summe = sum(liste1)
print(f"Summe: {Summe}")
durch = Summe / len(liste1)
print(f"Durchschnitt: {durch:.2f}")
