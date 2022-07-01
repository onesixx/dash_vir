import json

dictVal = {'name':'johnDou', 'age':16, 'job':True}

jsonVal = json.dumps(dictVal)
# '{"name": "johnDou", "age": 16, "job": true}'

dictVal2 = json.loads(jsonVal)
# {'name': 'johnDou', 'age': 16, 'job': True}

dictVal['name']
# 'johnDou'
jsonVal['name']
# TypeError: string indices must be integers 




---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Input In [29], in <cell line: 1>()
----> 1 jsonVal['name']

TypeError: string indices must be integers
dict1 = {'name':'song', 'age' : 10 }

print(f"dict1 = {type(dict1)}")

json_val = json.dumps(dict1)


print "json_val = %s" % json_val
print "json_val type = %s" % type(json_val)


import json
import requests

url = 'localhost:8000/api/example'

res = requests.get(url)
type(res.text)	# str
res.['key-name']	# 오류


res = json.loads(res.text)
type(res.text)	# dictionary

res.['key-name'] # 가능
