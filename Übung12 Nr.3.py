import math
def handshakes(n):
        h=(n*(n-1))/2
        return int(h)
    
for n in range(1,21):
        print(f"Anzahl Personen: {n:2} Anzahl Handshakes: {handshakes(n):6}")