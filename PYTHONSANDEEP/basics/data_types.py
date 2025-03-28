'''
Created on 25 Mar 2025

@author: Sandeep

Data type: category to which an i/o data belongs to.

Categorization of data helps us in memory allocation for efficient memory handling.
To check the comatibility b/w 2 data types

Q. Dynamic typing vs Static typing

Categories of data-types:
1. Built-in data-types: Data types already available in python
   a. Fundamental data types:
      i.   int
      ii.  float
      iii. complex - a+bj
      iv.  bool (boolean) - True or False
      v.   str (string) - "",' '
      
    b. non-fundamental data types:
       i.   list
       ii.  tuple
       iii. set
       iv.  dict
       v.   bytes
       vi.  bytearray
       
2. User defined data types: Data types which are created by programmer          

Commenting in Python:
1. Single line comments: - #
2. Multi line comments: - triple double/ single quotes.
'''
# int a = 3; --> java example
a = 3.0 # float
b = "abc" # string
c = 5 # integer
d = 4+7j # complex
e = True # boolean
# c = a+b
# print(c)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
# print(type(c))

