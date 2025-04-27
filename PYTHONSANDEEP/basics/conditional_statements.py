'''
Created on 29 Mar 2025

@author: Conditional statements
Statements check the conditions and determines the flow

If a condition is satisfied one set of code will executed otherwise another set of code can be executed.

Syntax:

If condition:
<code to be executed if condition is satisfied>

Indentation: (4 spaces or one tab space) 

Types of conditional statements:
1. if statement: if a condition is satisfied  one set of code will be executed otherwise it won't
2. if else 
3. series of if-else statements
4. nested of if-else statements



'''


age=int(input("Enter your age:"))

if age>=18 and age <=59:
    print("You're an adult")
    
elif age<18 and age>12:
    print("You're  an adolescent") 
    
elif age<12:
    print("You're a child")
else:
    print("You're a senior citizen")

      
if age>13:
    if age>59:
        print("Youre an ")
    else:
        print("You're an adult")
else:
    if age<13:
        print("You're a child")
    else:
        print("You're ")
    
'''
    
if age in range(0, 13):
    print("you're a child")
    
    elif age in range(14, 19):
    print("you're an adolescent")
    
    elif age in range(19, 60):
    print("you're an adult")
   ''' 
    


#if age>0:

    

    
    