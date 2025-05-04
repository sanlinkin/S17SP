'''
Created on 4 May 2025

@author: Sandeep
Methods are functions which are defined inside a class.
We can call methods using the objects of that class.
A method of one class can be called using an object of that class.

Contructor: (_init_): It is a magic method used to construct an object by initialize 
            specific values being passed while creating the object.
'''

#class MyClass():
'''
class HumanBeings():
    def walk(self):
        print("I am walking")
        print("I playing football")
obj1=HumanBeings()
obj1.walk()
'''
# name="chitra"
# name2="lakshmi"
# # A method of one class can be called using an object of that class.
# name.capitalize()
# print(type(name))




class HumanBeings():
    def __init__(self, name):  # _init_ indicates magic method or constructors
        self.name=name
    
    def walk(self):
        print(f"{self.name} is  walking")
        


obj1=HumanBeings("Vivek")
obj1.walk()

print(type(obj1)) # <class '__main__.HumanBeings'>

obj2=HumanBeings("Yash")
obj2.walk()
obj1.walk()




