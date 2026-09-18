l =[1,2,3,4,5,6]
n = int(input("Anzahl Rotationen>"))

neue_liste = l[-n:] + l[:-n]

print(neue_liste)