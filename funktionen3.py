def bubblesort(liste):
    for n in range (len(liste),1,-1):
        for i in range (0,n-1):
            if liste[i] > liste[i+1]:
                tausch = liste[i]
                liste[i] = liste[i+1]
                liste[i+1] = tausch
    return liste

zahlen=[5,7,8,22,3,1,0]

print(bubblesort(zahlen))