import math

#for

n = int(input("Eingabe> "))
f =1
for i in range(1,n+1):
    f = math.factorial(i)
    
print("Das Ergebnis ist: ",f)
print("*** Ende for ***")


#while

n = int(input("Eingabe> "))
f =1
i =1
while i<=n:
    f=f*i
    i+=1
print("Das Ergebnis ist: ",f)