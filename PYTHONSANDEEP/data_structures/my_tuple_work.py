'''
Created on 12 Apr 2025

@author: Sandeep

'''

# a. Creation of tuple
z = ()
print(type(z))

 
# b.  Creation of tuple with elements
y=(1, 2, 3, 4, 5) # Homogeneous data structure
print(y)
print(type(y))


x=(2, "abc", 5.76, False, 5+8j) # Heterogeneous data structure
print(x)
print(type(x))

w = 1, 5j+4 , 4.5, True # parenthesis are optional for Tuple
print(w)
print(type(w))

v = tuple(range(1, 20))
print(v)

u = ('Neymar')
print(u)
print(type(u))

t = (10)
print(t)
print(type(t))

# By using tuple() function
y2 = [10, 20, 30, 40, 50]
s=tuple(y2)
print(s)

"<====Different ways to access Tuple====>"
#Indexing
#Slicing operator
#looping

#Accessing Tuples using indexing (access single element)
#indexing
print(y2[0]) #positive indexing
print(y2[-1]) #negetive indexing

#Accessing Tuples using slicing operator (access range of element)
#Slicing operator
print(y2[2:5])
print(y2[2:70])
print(y2[::3])

#Accessing Tuples using looping 
for i in y2:
    print(i)

# Tuple immutability (cannot modify or replace)

#mathematical operator
#Concatenation operator (+)
#Multiplication operator (*)


# concatenation operator (+)
s=(1,2,3,4)
r=(4,6,7,8)
q=s+r
print(q)
# Multiplication operator (*)
p=s*5
print(p)




















        
   



