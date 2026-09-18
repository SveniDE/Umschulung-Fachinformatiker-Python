import json
do = open("einwohnerdatei.json","r",encoding="utf-8")
dict1=json.load(do)
do.close()

for k,v in dict1.items():
    if v==None : v="-----"
    print(k,v)