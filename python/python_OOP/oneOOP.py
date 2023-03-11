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

class Student:

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0_> 100
        
    def get_grade(self):
        return self.grade
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

class Course:

    def __init__(self, nameCourse, maxNum):
        self.nameCourse = nameCourse
        self.maxNum = maxNum
        self.students = []
        self.is_active = False
        
    def get_students(self):
        list_student = ""
        num = len(self.students)
        count = 0
        for i in range(num):
            list_student += f"\t{i+1} -> {self.students[i].name}"
            count += 1
            if count != num:
                list_student += "\n"
        print(f"----All student in this {self.nameCourse}----")
        print(list_student)

    def add_student(self, student):

        if len(self.students) < self.maxNum:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        total = 0
        for student in self.students:
            total += student.get_grade()

        return total/len(self.students)
        
class Pet: #parent class
    def __init__(self, name, animal, age, owner):
        self.name = name
        self.animal = animal.lower()
        self.age = age
        self.owner = owner

    # Template
    def speak(self):
        print("**Animal language**")

    def introduce(self):
        print(f"\tMy name is {self.name}")
        print(f"\tI'm a {self.animal}")
        print(f"\tMy owner's name is {self.owner}.")
    

class Cat(Pet): # Inherit from Pet class #child class

    def __init__(self, name, age, owner):
        super().__init__(name, "cat", age, owner)

    def speak(self):
        print("Meow!")

class Dog(Pet):
    def __init__(self, name, age, owner):
        super().__init__(name, "dog", age, owner)

    def speak(self):
        print("Woof Woof!")

class Fish(Pet):
    def __init__(self, name,  age, owner):
        super().__init__(name, "fish", age, owner)
    
class Person:
    num_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_people(cls):
        # cls acting on this class
        return cls.num_of_people

    @classmethod
    def add_person(cls):
        cls.num_of_people +=1

class Math:
    @staticmethod
    def add5(num):
        return num + 5

    @staticmethod
    def add10(num):
        return num + 10

    @staticmethod
    def sum(num1,num2):
        return num1+num2

def sectionOne():

    print("--------------------------")
    #Basis of OOP
    animalOne = Animal("Dog")
    print(animalOne.get_name())
    print(type(animalOne))
    animalOne.eat()

    animalTwo = Animal("Cat")
    print(animalTwo.get_name())
    animalTwo.set_name("Parrot")
    print(animalTwo.get_name())
    
    print("--------------------------")

def sectionTwo():
    s1 = Student("Jill", 18, 50)
    s2 = Student("Kim", 19, 45)
    s3 = Student("Bill", 18, 60)
    s4 = Student("Hilton", 19, 75)

    science_course = Course("Science", 20)
    #Add Object in Object
    print("Add successfully: ", science_course.add_student(s1))
    print("Add successfully: ", science_course.add_student(s2))
    science_course.get_students()
    print(f"Average grade of this course: {science_course.get_average_grade()}")

def sectionThree():
    #Inheritance
    pet1 = Pet("Steve", "Cat", 1,"Billy")
    pet1.introduce()
    print()
    catOne = Cat("Angel", 2, "Bob")
    catOne.introduce()
    print()
    dogOne = Dog("Mike", 3, "Hilton")
    dogOne.introduce()
    print()
    bob = Person("Bob")
    jill = Person("Jill")
    print(f"\t{bob.number_of_people()}")

def main():
    print("-------------------------------\n")
    path = "https://www.youtube.com/watch?v=JeznW_7DlB0"

    print("\tYoutube: tech with tim\n\tDivided into 3 sections")
    print("\tSection 1 -> Basic Object (Initialize, self keyword)")
    print("\tSection 2 -> Object in object")
    print("\tSection 3 -> Inheritance")
    print(f"\tLecture from : {path}\n")
    print("-------------------------------")
main()
# create a main function
