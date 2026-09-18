while True:
    n = int(input("Zahl>"))
    if n<=0: break
    qs = 0
    for s in str(n): qs=qs+int(s) # Quersumme in einer Zeile berechnen!
    print("Quersumme:",qs)
 
 
print("*** Programmende ***")