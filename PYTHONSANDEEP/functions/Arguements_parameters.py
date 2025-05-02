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
1. Positional arguments
    - Actual arguments which are assigned to formal arguments based on their positions
2. Keyword arguments
    -  Actual arguments which are assigned to formal arguments using key-value pair
'''
def subtraction(a, b):
    c=a-b
    print("a=", a)
    print("b=", b)
    print("c=", c)
    
subtraction(20, 10) # a=20; b=10
subtraction(10, 20) # a=10; b=20
subtraction(b=10, a=20)



    