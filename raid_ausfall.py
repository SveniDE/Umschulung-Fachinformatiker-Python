import random as r
mtbf = 100  # Ausfallwahrscheinlichkeit 1/mtbf
samples = 100000  # Durchläufe

# RAID 5 mit 3 HDD
ausfälle = 0
for i in range(samples):
    defekt = 0  # merken wieviel HDDs defekt sind
    for hdd in range(3):    # 3 Durchläufe
        if r.randrange(0, mtbf) == 0:   # wenn HDD defekt
            defekt += 1
    if defekt >= 2: ausfälle += 1   # ab 3 defekte HDD -> Ausfall + 1

print(ausfälle/samples*100)

# RAID 6 mit 4 HDD
ausfälle = 0
for i in range(samples):
    defekt = 0  # merken wieviel HDDs defekt sind
    for hdd in range(4):    # 3 Durchläufe
        if r.randrange(0, mtbf) == 0:   # wenn HDD defekt
            defekt += 1
    if defekt >= 2: ausfälle += 1   # ab 4 defekte HDD -> Ausfall + 1

print(ausfälle/samples*100)