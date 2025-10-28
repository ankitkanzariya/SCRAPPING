import json

person = {"name": "Ankit", "age": 22, "skills": ["Python", "Django"]}

json_str = json.dumps(person)
print("JSON string:", json_str)

person2 = json.loads(json_str)
print("Back to dict:", person2)
print("Name:", person2["name"])
print("Skills:", person2["skills"])

