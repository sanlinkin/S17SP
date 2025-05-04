'''
Created on 27 Apr 2025

@author: Sandeep

Function: Is a block of code which can be reused
OR 
Function is a block of reusable code

Ex: print(), type(), input(), id()...etc. 

Types of functions:
1. Predefined functions. came as part of python package
    - bultin functions
2. User-defined functions: are defined by users

Why we need fuctions?
1. Reduce repeatition of code/ Reduce complexity, minimize the no. of lines of code. This helps in increased code readability
2. Easy maintenance

Syntax:
def fuction_name(parameters):
    <code>
def -> keyword to define function (mandatory)
fuction_name -> lower case words separated by _ (mandatory)
(): -> mandatory
parameters -> variables to accept/consume  the values passed by the user (not mandatory)

Types:
1. Function without parameters
2. Function with parameters

'''
a=2
b=5
c=a+b 
print(f"sum of {a} and {b}:", c)

a=6
b=7
c=a+b
print(f"sum of {a} and {b}:", c)

# Function without parameters
def welcome():
    print("Hello User! Welcome to iQuest!")
    print("I hope you're doing great!")
    
welcome()
#welcome()
#welcome()
#welcome()


# Function with parameters
def addition(a, b): # a, b called as parameters
    c=a+b
    #print(f"addition of {a} and {b}:", c)
    return c
    
d=addition(10, 20) # user gives values for 'a' and 'b'
print(d)
# OR
print(addition(8,10))

def multiplication(num,multiplier):
    result_mul=num*multiplier
    #print(result_mul)
    return result_mul 
multiplication(d, 5) 
#or 
# multiplication(addition(10,20), 5)


def division_integer_division(dividend, divisor):
    div_quotient = dividend/divisor
    int_div_quotient = dividend//divisor
    return div_quotient, int_div_quotient
    
div_output1,div_output2 =division_integer_division(7, 2)
print(div_output1)
print(div_output2)



f, g=5,6
print(f)
print(g)

def add_mul(a, b):
    add_op=addition(a, b) # calling one function inside another function
    mul_op=multiplication(a,b)
    return add_op, mul_op
    
print(add_mul(5, 3))





