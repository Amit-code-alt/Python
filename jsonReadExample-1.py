import json

data ={
    "name" : "Amit kumar",
    "age"  : "26",
    "Location" : "Mumbai",
    "company" : "Azentio",
    "skills" : ["Python","sql","powerbi"]
}

# convert json to string
stringjson = json.dumps(data,indent=2)
print("Json Conversion ",stringjson)