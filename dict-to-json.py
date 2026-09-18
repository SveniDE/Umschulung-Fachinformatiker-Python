import json
pdict={'Name':'Fritz','bezahlt':True, 'hobbies':None}
do = open("test.json","w")
json.dump(pdict,do,indent=5)