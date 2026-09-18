PI=3.1416

r1=float(input("Aussenradius> "))
r2=float(input("Innenradius> "))

# f1=PI*r1**r1
# f2=PI*r2**r2

# f_gesamt=f1-f2

f_gesamt=PI*(r1**2-r2**2)

print("Ringfläche ist: " , f_gesamt)
