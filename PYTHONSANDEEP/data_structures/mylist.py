'''
Created on 6 Apr 2025

@author: Sandeep


Data Structures:

* Variable stores only one data
  a=1
* A data structure is an entity which stores multiple data elements.
* Type:
    1. list - []
    2. tuple - ()
    3. set
    4. Dictionary - {}
'''
'''
list: is a data structure represented by []


1. creation of list
    - Empty list can be created
    - List with elements
        > Manually adding elements
        > Using in-buldi function called list
2. List is heterogeneous 
    
'''
# a. creation of list


a = []
print(type(a))

# b.  Creation of list with elements
b=[1, 2, 3, 4, 5] # Homogeneous data structure
print(type(b))
print(b)

c=[1, "abc", 4.76, True, 3+8j] # Heterogeneous data structure
print(c)

c={1:"vivek"}

print(c)

d=list(range(10))
print(d)



