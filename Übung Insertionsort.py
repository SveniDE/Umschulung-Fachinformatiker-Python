import random

def insertionSort(liste: list) -> list:   # mit Type Hints
    for i in range(1,len(liste)):
        einzusortierender_wert = liste[i]
        j = i
        while j > 0 and liste[j - 1] > einzusortierender_wert:
            liste[j] = liste[j - 1]
            j -= 1  # j=j-1
        liste[j] = einzusortierender_wert
    return liste

liste=[]
for i in range(20000):
    liste.append(random.randint(1,100000))

print("Sortiere...")
liste=insertionSort(liste)
print(liste[0:10])