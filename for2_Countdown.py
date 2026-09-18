# for-Schleife mit Schrittweite
import time

for i in range(1,10,2):
   print(i)

print("*** Ende ***")
print("")

for i in range(10,-1,-1):
    print(i)
    time.sleep(1) # Aus Modul time die Methode sleep

print("*** Feuer ***")
