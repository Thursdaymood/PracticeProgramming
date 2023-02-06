class Animal:

    #Initialize object
    def __init__(self, name):
        self.name = name
    
    #Get Method
    def get_name(self):
        return self.name
    
    #Set Method
    def set_name(self, newName):
        self.name = newName
        
    #Method
    def sleep(self):
        print(f"This {self.name} is sleeping.")

    
    def eat(self):
        print(f"This {self.name} is eating.")

def main():
    print("--------------------------")
    animalOne = Animal("Dog")
    print(animalOne.get_name())
    print(type(animalOne))
    animalOne.eat()

    animalTwo = Animal("Cat")
    print(animalTwo.get_name())
    animalTwo.set_name("Parrot")
    print(animalTwo.get_name())
    



    print("--------------------------")
main()