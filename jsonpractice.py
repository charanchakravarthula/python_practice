# importing json
import json
json_format={'a':1,'b':2,'c':3}
# converting dict to json string
p=json.dumps(json_format)
print(p,type(p))
# cob=nverting json string to dict
q=json.loads(p)
print(q,type(q))


