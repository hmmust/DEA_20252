import json
f1 = open("students.json","rt")
students = json.load(f1)
print(students)
f1.close()

