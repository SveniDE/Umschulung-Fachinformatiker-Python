import csv
überschrift=["Name", "Entf.Sonne(AE)", "Radius(km)", "Monde"]

merkur = ["Merkur", 0.39, 2440, 0]
venus = ["Venus", 0.72, 6052, 0]
erde = ["Erde", 1.0, 6378, 1]
mars = ["Mars", 1.52, 3397, 2]
jupi = ["Jupiter", 5.2, 71493, 79]
saturn = ["Saturn", 9.54, 60267, 82]
uranus = ["Uranus", 19.19, 25559, 27]
neptun = ["Neptun", 30.07, 24764, 14]

planetentabelle= []

planetentabelle.append(merkur)
planetentabelle.append(venus)
planetentabelle.append(erde)
planetentabelle.append(mars)
planetentabelle.append(jupi)
planetentabelle.append(saturn)
planetentabelle.append(uranus)
planetentabelle.append(neptun)

# print(f"| {überschrift[0]:7} | {überschrift[1]:12} | {überschrift[2]:8} | {überschrift[3]:3} |")
# print("-----------------------------------------------------------------------------------")
# for p in planetentabelle:
#     print(f"| {p[0]:7} | {p[1]:12} | {p[2]:8} | {p[3]:3} |")

print(f"| {überschrift[0]:<8} | {überschrift[1]:>13} | {überschrift[2]:>8} | {überschrift[3]:>5} |")
print("-" *50)
for p in planetentabelle:
    print(f"| {p[0]:<8} | {p[1]:>13} | {p[2]:>8} | {p[3]:>8} |")

datei = open("planeten.csv","w",encoding="utf-8")
writer = csv.writer(datei,delimiter=";",lineterminator="\n",quoting=csv.QUOTE_NONNUMERIC)
writer.writerow(überschrift)
writer.writerows(planetentabelle)
datei.close()