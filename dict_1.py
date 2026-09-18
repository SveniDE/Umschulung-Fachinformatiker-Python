# Dictionary mit 3 key:value Paaren
# Ein Dict immer in geschweiften Klammern
# Den "key" immer in Anführungszeichen
# Der "key" muss immer einzigartig/eindeutig sein pro Dict.
person1 = {"name":"Hans", 
           "alter":23, 
           "kurs":"FIAE", 
           "bezahlt":True}

person2 = {"name":"Britta", 
           "kurs":"FISI", 
           "alter":25, 
           "bezahlt":False}

personen = [{"name":"Otto","alter":45}, {"name":"Klara","alter":55}, {"name":"Karl","alter":78}]

for d in personen:
    print(d["name"],d["alter"])