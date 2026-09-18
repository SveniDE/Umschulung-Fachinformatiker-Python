import json

tn1 = {"name":"Otto Meier",
       "alter":32,
       "hobbies":["Fußball","Schach","Chillen"]}

do = open("teilnehmer.json","w",encoding="utf-8")
json.dump(tn1,do,indent=5)
do.close()