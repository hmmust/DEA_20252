import json

students  =[ {"name":'Raghad',"age":22,"married":False,"courses":["GP1","BDA"]},
            {"name":'Nedal',"age":21,"married":False,"courses":["DEA","BDA"]},
            {"name":'Janna',"age":21,"married":False,"courses":["RP","BDA"]},
           ]
f1 = open("students.json","wt")
json.dump(students,f1)
f1.close()

students2  ={ "name":['Raghad','Nedal','Janna'],
             "age":[22,21,21],
             "courses":[["GP1","BDA"],["DEA","BDA"],["RP","BDA"]]}

f2 = open("students2.json","wt")
json.dump(students2,f2)
f2.close()