'''
Created on 2 May 2025

@author: Sandeep


Arguments = parameters

1. Formal arguments: parameters which are declared while defining a function
    - Formal arguments collects/accepts values (actual arguments) when a function is called
2. Actual arguments: actual values passed while calling a function

Ex:  
def addition(a, b): # a, b are formal arguments
    c=a+b
    return c
    
d=addition(10, 20) # 10, 20 are actual arguments
print(d)

Types of Actual arguments:
1. Positional arguments:
    - Actual arguments which are assigned to formal arguments based on their positions
2. Keyword arguments:
    -  Actual arguments which are assigned to formal arguments using key-value pair

Types of formal arguments:
1. Default arguments
2. Variable length arguments # stores in the form of tuple
3. Keyword variable length arguments(**) # stores in the form of dictionary


'''

def subtraction(a, b):
    c=a-b
    print("a=", a)
    print("b=", b)
    print("c=", c)
    
#subtraction(20, 10) # a=20; b=10
#subtraction(10, 20) # a=10; b=20
#subtraction(b=10, a=20)

#E=mc**2
def cal_energy(m, c=300000000):
    e=m*c**2
    print("Energy in joules:", e)

# cal_energy(5)
# cal_energy(3)

def addition(*a): 
    print(sum(a))
    print(type(a))
    
# addition()
# addition(1)
# addition(5, 6)
# addition(6, 7, 8, 9)

'''
(sum of tuple using for loop)
b=(3, 4, 5, 6, 7)
#print(sum(b))
# OR
result=0
for num in b
'''    
def display(**x):
    print(x)

#display(name="Sandeep", age=12, gender="male")




    
    
    

    