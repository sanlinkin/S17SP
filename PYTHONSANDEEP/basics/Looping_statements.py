'''
Created on 1 Apr 2025
@author: SANDEEP:
Looping Statements:
Statements which executes a code multiple times until a condition is satisfied:

Types:
1. While loop
    a. intialisation of a variable
    b. while condition >> while block
    c. increment/ decrement
2. for loop: iterate over collections/ range

Loop control statements
1. break -(Will terminate the execution of Loop)
2. continue - (It skips the execution of Loop for once)
Pass statement: Doesn't perform any operations. It is added to make program syntactically 

range(start, stop, step)


'''
'''
count=0

while count<5:
 
    #print(count)
    #print("count<5", count<5)
    print("Hello World!")
    #count=count+1
    count+=1 # increment operator: +=; decrement operator: -=
    
#print("count:",count)    
#print("count<5: ",count<5)

count=5

while count>0:
 
    print("Hello World!")
    #count=count-1
    count-=1 #  decrement operator: -=
  
count=2.1

while count>0:
    #print(count)
    #print("count<5", count<5)
    print("Hello World!")
    #count=count+1
    count-=1

while True:
    print("Hello World!")

while True:
    pass
print("The end")  
  
count=0
while count<=100:
    if count == 50:
        count+=1
        continue
    print(count)   
    count+=1
    
#print(range(10))

for n in range (1, 100):
    if n == 50: 
        continue
    print(n) 
    
for n in range (0, 100): #print only even numbers from 0 to 100
    if n%2 == 0:
        if n == 6:
            continue
        print(n) 
        
    
for n in range(0, 100, 2): #(printing 2 steps every time)
    print(n) 
   
  
for n in range(1, 6):
    print("*", end=" ") #(end=" "stays in same line)


1)Upward right angled triangle
  
for n in range(1, 6):
    
    for n in range(n):
        print("*", end="")
        
    print() 


(results)
*
**
***
****
*****
'''
'''
  
  row number/ no. of stars  
  1 / 5
  2 / 4
  3 / 3
  4 / 2
  5 / 1
  

2)Invert or downward right angled triangle
for n in range(5, 0, -1):
    
    for n in range(n):
        print("*", end=" ")
    
    print()
    
Results
* * * * *
* * * *
* * *
* *
*
      OR 
for n in range(1, 6):

    for n in range(6-n):
        print("*", end=" ")
    
    print()
    
''' 
#Stop valve (6)
#Row no. (1)
#No. of stars(5) #stop value- row No.
'''

3)

    *
   * *
  * * *
 * * * *
* * * * *


*
* *
* * *
* * * *
* * * * *


1111*
111* *
11* * *
1* * * *
* * * * *
'''

for n in range(1, 6):
    
    for m in range(6-n):
        print(" ", end="")
    
    for i in range(n):
        print("*", end=" ")
        
    print() 



    
    
    

