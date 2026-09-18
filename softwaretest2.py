def insertSort(liste):
    for i in range(1,len(liste)):
        ew = liste[i]
        j = i
        while j>0 and liste[j-1] > ew:
            liste[j] = liste[j-1]
            j = j-1
        liste[j] = ew
    return liste

def test_insertSort():  # Testunit für die Funktion insertSort
    assert insertSort([5,2,9,1,5,6]) == [1,2,5,5,6,9]
    assert insertSort([3,0,-1,8,7]) == [-1,0,3,7,8]
    assert insertSort([]) == []
    assert insertSort([1]) == [1]
    assert insertSort([2,1]) == [1,2]
    assert insertSort([1,2]) == [1,2]
    assert insertSort([5.6,1]) == [1,5.6]
    assert insertSort(["B","A"]) == ["A","B"]
    print("All tests passed.")

test_insertSort()   # Aufruf der Testfunktion, um die Tests auszuführen