import math
def kubik(x):
    erg = x**3
    return erg

def anzahlHosts(nbits):
    hosts=2**(32-nbits)-2   # minus 2 wegen Broadcastadresse und Netzwerkadresse
    return hosts

#Main
# for i in range(1,51):
#    print(i, kubik(i))

for i in range(0,32):
    print("Netzwerkbits:",i, "Hosts:",anzahlHosts(i))