import json
 
dict = {'name':'lei','sex':'name'}
 
jsonstr = json.dumps(dict)
filename = open('/home/ljiang/Desktop/jsonFile.json','w')#dict转josn
filename.write(jsonstr)
