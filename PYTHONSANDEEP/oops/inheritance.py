'''
Created on 7 May 2025

@author: Sandeep

Inheritance: Carry forwarding properties (features & functions) from one class to another class.

Parent/ Super class: From which class property is being inherited (Ex: HumanBeings)

Child/ sub class: To which a property is being inherited. (Ex: Male class, Female class)

How we can check?
From object perspective, an object created from a child class should be able to access/ call them
properties from its parent class.

Why we need inheritance?
- It reduce repetition and increase code reusability which helps us in easy maintenance. 

Types of inheritance:
1. single level inheritance
2. Multi-level inheritance
3. Multiple inheritance

Method Resolution order(mro):In an inheritance when we call a method using an object MRO 
        will helps python interpretor to decide in which order it has to traverse the classes.

Super(): This is used to call super class/ parent class constructor or methods to child class 
        when there is a constructor OR a method present in child with same name as super class.
'''
'''
class GrandFather:
    def gf_method(self):
        print("This is Grand father method")
        
class Mother(GrandFather):
    def m_method(self):
        print("This is Mother method")

class Father:
    def f_method(self):
        print("This is Father method")
        
class Child(Mother, Father):
    def c_method(self):
        print("This is Child method")

print("====GrandFather Class====")        
ajja=GrandFather()    
ajja.gf_method()

print("====Mother Class====") 
amma=Mother()
amma.m_method()
amma.gf_method()

print("====Child Class====") 
paapu=Child()
paapu.c_method()
paapu.gf_method()
paapu.m_method()
paapu.f_method()
'''
'''
# 08/05/2025---> online class

class GrandFather:
    def __init__(self):
        print("This is Grand father class constructor")       
    def gf_method(self):
        print("This is Grand father method")
 
         
class Mother(GrandFather):
    def __init__(self):
        print("This is Mother class constructor")    
    def m_method(self):
        print("This is Mother method")    
    def c_method(self):
        print("This is mother class method")
    def car(self):
        print("This is Mother's car")   
 
                        
class Father:
    def f_method(self):
        print("This is Father method")
    def car(self):
        print("This is Father's car")
 
        
class Child(Father, Mother):
    def __init__(self):
        print("This is Child class constructor")
        
    def c_method(self):
        print("This is Child class c_method")

print("====GrandFather Object====")        
ajja=GrandFather()    
ajja.gf_method()

print("====Mother Object====") 
amma=Mother()
amma.m_method()
amma.gf_method()
amma.c_method()

print("====Child Object====") 
paapu=Child()
paapu.c_method()
paapu.gf_method()
paapu.m_method()
paapu.f_method()
paapu.car()

print("=====Method Resolution Order(MRO)=====")
print(Child.mro())
'''
'''
# 10/05/2025 Offline class

class GrandFather:
    def __init__(self):
        print("This is Grand father class constructor")       
    def gf_method(self):
        print("This is Grand father method")
 
         
class Mother(GrandFather):
    
    def __init__(self):
        print("This is Mother class constructor")    
    def m_method(self):
        print("This is Mother method")    
    def c_method(self):
        print("This is mother class method")
    def car(self):
        print("This is Mother's car")   
 
                        
class Father:
    def f_method(self):
        print("This is Father method")
    def car(self):
        print("This is Father's car")
 
        
class Child(Father, Mother):   #(): and #(Father, Mother):
    def __init__(self):
        print("This is Child class constructor")
        
    def c_method(self):
        print("This is Child class c_method")

print("====GrandFather Object====")        
ajja=GrandFather()    
ajja.gf_method()

print("====Mother Object====") 
amma=Mother()
amma.m_method()
amma.gf_method()
amma.c_method()

print("====Child Object====") 
paapu=Child()
# paapu.c_method()
# paapu.gf_method()
# paapu.m_method()
# paapu.f_method()
# paapu.car()


print("=====Method Resolution Order(MRO)=====")
print(Child.mro())

print("======Directory - dir()=======")
print(dir(paapu))
'''

class GrandFather:
    def __init__(self, name):
        print("Object created with name: ", name)       
    def gf_method(self):
        print("This is Grand father method")
 
         
class Mother(GrandFather):
    
    def __init__(self, name, age):
        #print(f"Object is created with name: {name} and age: {age}") 
        # OR
        super().__init__(name) # super class keyword is used to call super class method 
        print(f"Age of {name} is {age}")
    def m_method(self):
        print("This is Mother method")    
    def c_method(self):
        print("This is mother class method")
    def car(self):
        print("This is Mother's car")   
 
                        
class Father:
    def f_method(self):
        print("This is Father method")
    def car(self):
        print("This is Father's car")
 
        
class Child(Father, Mother):   #(): and #(Father, Mother):
    '''
    def __init__(self, name):
        print("This is Child class constructor")
     '''   
    def c_method(self):
        print("This is Child class c_method")

print("====GrandFather Object====")        
ajja=GrandFather("ajja")    
# ajja.gf_method()

print("====Mother Object====") 
amma=Mother("amma", 50)
# amma.m_method()
# amma.gf_method()
# amma.c_method()

print("====Child Object====") 
paapu=Child("paapu", 25)
# paapu.c_method()
# paapu.gf_method()
# paapu.m_method()
# paapu.f_method()
# paapu.car()
