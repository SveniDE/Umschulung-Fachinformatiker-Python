import json

preise = {"Apfel":0.49,
"Banane":0.39,
"Kaffee":5.99,
"Schokolade":1.49,
"Milch":1.19,
"Eier":2.79,
"Butter":2.39,
"Brot":2.99,
"Reis":1.89,
"Nudeln":1.29,
"Käse":3.49,
"Tomaten":2.59,
"Gurke":1.29,
"Mineralwasser":0.79,
"Saft":1.99,
"Pizza_Napoli":3.79}

preise["Pfirsiche"] = 1.25

preise.pop("Saft")

print(f"Produkt          Preis")
print(f"----------------------")
for k,v in sorted(preise.items()):
    
    print(f"{k:14}  {v:5} €")


do = open("preise.json","w",encoding="utf-8")
json.dump(preise,do,indent=2,ensure_ascii=False)
do.close()