import csv

datei = open("planeten.csv","r",encoding="utf-8")
reader = csv.reader(datei,delimiter=";",lineterminator="\n",quoting=csv.QUOTE_NONNUMERIC)

for p in reader:
    print(f"| {p[0]:<8} | {p[1]:>13} | {p[2]:>8} | {p[3]:>8} |")

datei.close()