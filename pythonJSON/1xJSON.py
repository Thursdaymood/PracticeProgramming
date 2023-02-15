import json
#Ref : NeuralNine
# JSON -> Javascript Object Notation
# is a text format for string and transporting data
# used to send data between computers
# 
mydict = {
    "People" : [
        {"name" : "Bob", "age" : 28,"weight" : 80},
        {"name" : "Anna", "age": 34, "weight": 67},
        {"name" : "Charles", "age" : 18,"weight" : 45},
        {"name" : "Daniel", "age": 20, "weight": 58}
    ]
}

def convertToJSON(data):

    json_string = json.dumps(data, indent = 1)
    with open("mydata.json","w") as f:
        f.write(json_string)

def convertToPython(data):
    with open(data, "r") as f:
        json_object = json.loads(f.read())

    print(json_object["People"][0]["name"])

convertToPython("mydata.json")