import csv
do = open("geburtstage.csv","r",encoding="utf-8")
reader = csv.reader(do, delimiter=";", quoting=csv.QUOTE_NONE)
head=next(reader)   # Überschrift auslesen

for z in reader:    # Daten auslesen
    print(f"{z[0]:3} {z[1]:12} {z[2]:12} {z[3]:10}")