import math
pi=math.pi
r = float(input("Wie groß ist der Radius? "))
v=(4/3)*pi*r**3
o=4*pi*r**2

print("Der Radius ist: ",r, ", das Volumen: ",round(v,2),"und die Oberfläche: ", round(o,2))
