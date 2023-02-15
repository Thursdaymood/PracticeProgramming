# person class

import json
class Person:
    def __init__(self,name,age,country):

        self.name = name
        self.age = age
        self.country = country

    def print_info(self):
        print(f"Hello my name is {self.name}.")
        print(f"I'm {self.age} years old.")
        print(f"I'm from {self.country}.")

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_country(self):
        return self.country

    def save_to_JSON(self, fileName):
        #arrange the data in dictionary
        person_dict = {"name" : self.name, "age" : self.age, "country" : self.country}

        # Use method dump to convert data into JSON type
        with open(fileName, "w") as f:
            f.write(json.dumps(person_dict, indent =2))

    def load_from_JSON(self, fileName):
        with open(fileName, "r") as f:
            data = json.loads(f.read())
        self.name = data["name"]
        self.age = data["age"]
        self.country = data["country"]


personOne = Person("Sin", 19, "Thailand")
personOne.print_info()
personOne.save_to_JSON("personal_info")

personTwo = Person(None, None, None)
personTwo.save_to_JSON("Sin")
personTwo.load_from_JSON("Sin")
