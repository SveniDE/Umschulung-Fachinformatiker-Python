import json

do = open("kurs.json","r",encoding="utf-8")
dict1 = json.load(do)
do.close()

print("Kurs:             ", dict1["kursname"])
print("Teilnehmer:       ", dict1["teilnehmer"])
print("Raum:             ", dict1["raum"])
print("Online-Kurs:      ", dict1["online"])


if dict1["teilnehmer"] >15:
    print("Der Kurs hat mehr als 15 Teilnehmer")