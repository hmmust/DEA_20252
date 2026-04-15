import json

raghad  = {"name":'Raghad',
           "age":22,
           "married":False,
           "courses":["GP1","BDA"]}

raghad_json = json.dumps(raghad)
print(type(raghad_json))
print(raghad_json)

f1 = open("raghard.json","wt")
json.dump(raghad,f1)
f1.close()