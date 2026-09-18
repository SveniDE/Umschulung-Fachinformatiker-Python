import json

itgeräte = {"geraet":"Notebook",
             "hersteller":"Dell",
             "preis":899.99,
             "defekt":True}

itgeräte2 = {"geraet":"Desktop",
             "hersteller":"hp",
             "preis":399.99,
             "defekt":True}

geraete = [{"geraet":"Notebook",
             "hersteller":"Dell",
             "preis":899.99,
             "defekt":True},
             {"geraet":"Desktop",
             "hersteller":"hp",
             "preis":399.99,
             "defekt":True}]

do = open("geraete.json","w",encoding="utf-8")
json.dump(geraete,do,indent=5)
do.close()