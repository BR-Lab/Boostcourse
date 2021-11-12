import json

dict_data = {"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]}

with open("json_example.json", "w") as f:
    json.dump(dict_data, f)

with open("json_example.json", "r", encoding='utf8') as f:
    contents = f.read()
    json_data = json.loads(contents)
    print(json_data["employees"])