import json
do = open("test.json","r")
pdict=json.load(do)
do.close()

print(pdict)