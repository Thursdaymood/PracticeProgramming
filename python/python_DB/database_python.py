# Incomplete

import sqlite3

class Person:
    def __init__(self, firstname="",lastname="",age=-1,id_person=-1): # set the default into null
        #create an connection
        self.connection = sqlite3.connect("testDB.db")
        #create medium to communicate
        #using python to communicate with database have to use cursor
        self.cursor = self.connection.cursor() 

        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.id_person = id_person

    def load_person(self, id_number):
        #display all data in table in form of list
        self.cursor.execute(
            """
            select * from persons
            where id_person = {}
            """.format(id_number))
        
        #create the variable 
        # to keep the data and the data will store in list type
        results = self.cursor.fetchone() # list
        print(results)
        self.id_person = id_number
        self.firstname = results[1] 
        self.lastname = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("""
            insert into persons
            values ({},"{}","{}",{})
        """.format(self.id_person,self.firstname,self.lastname,self.age))

        self.connection.commit()
        self.connection.close()

# connection = sqlite3.connect("testDB.db")
# cursor = connection.cursor()
# #create table
# cursor.execute("""
#     create table if not exists persons(
#     id_person int(100) not null,
#     first_name varchar(50),
#     last_name varchar(50),
#     age int(100)
#     )
# """)

# p1 = Person(7,"Alex","Robbin",30)
# p1.insert_person()


# cursor.execute("Select * from persons")
# results = cursor.fetchall()
# print(results)



