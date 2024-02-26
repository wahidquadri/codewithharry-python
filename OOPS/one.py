# Creating a class and object 

'''
class Student:            # creating a class
    name = "vahid"
    
s1 = Student()
print(s1.name)             # creating a object

s2 = Student()
print(s2.name)
'''

'''
class Car:
    colour = "blue"    # creating a class
    brand = "BMW"

car1 = Car()
print(car1.colour)     # crreating a object
print(car1.br)
'''

# Using constructor i mean using __init__ function 

class Student:
    def __init__(self,fullname):
        self.name = fullname
        print("adding new student in Database..")        

s1 = Student("vahid")
print(s1.name)
 