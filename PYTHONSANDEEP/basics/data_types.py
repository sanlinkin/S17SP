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
a = 3.65 # float
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

#Type Conversion/ Type casting
print('=======Type casting=======')
f = int(a) # o/p: 3 -> int
print(f)
print(type(f)) # conversion of float into integer

f = float(a) # o/p: 3.65 -> float
print(f)
print(type(f)) # conversion of float into float

f = str(a) # o/p: 3.65 -> str 
print(f)
print(type(f)) # conversion of float into string

f = complex(a) # o/p: 3.65+0j -> complex
print(f)
print(type(f)) # conversion of float into complex

f = bool(a) # o/p: True -> bool
print(f)
print(type(f)) # convervsion of float into boolean

'''
f = int(b) # o/p: error
print(f)
print(type(f)) # conversion of string into integer 


#f = float(b) #o/p: error
#print(f)
#print(typr(f)) # conversion of string into float

f = str(b) #o/p: abc -> str
print(f)
print(type(f)) # conversion of string into string

 f = complex(b) #o/p: error
 print(f)
 print(type(f))# conversion of string into complex
 '''
 
f = bool(b) #o/p: True -> bool
print(f)
print(type(f)) # conversion of string into boolean

f = int(c) #o/p: 5 -> int
print(f)
print(type(f)) # conversion of integer into integer

f = float(c) #o/p: 5.0 -> float
print(f)
print(type(f)) # conversion of integer into float

f = str(c) # o/p: 5 -> str
print(f)
print(type(f)) # conversion of integer into string

f = complex(c) # o/p: 5+0j -> complex
print(f)
print(type(f)) # conversion of integer into complex

f = bool(c) # o/p: True -> bool
print(f)
print(type(f)) # conversion of integer into boolean

'''
f = int(d) #o/p: error
print(f)
print(type(f)) # conversion of complex into integer

 f = float(d) #o/p: error
 print(f)
 print(type(f)) # conversion of complex into float
 '''

f = str(d) #o/p: 4+7j -> str
print(f)
print(type(f)) # conversion of complex into string

f = complex(d) #o/p: 4+7j -> complex
print(f)
print(type(f)) # conversion of complex into complex

f = bool(d) #o/p: True -> bool
print(f)
print(type(f)) # conversion of complex into boolean

f = int(e) #o/p: 1 -> int
print(f)
print(type(f)) # conversion of boolean into integer

f = float(e) # 1.0 -> float
print(f)
print(type(f)) # conversion of boolean into float

f = str(e) # o/p: True -> str
print(f)
print(type(f)) # conversion of boolean into string

f = complex(e) # o/p: 1+0j -> complex
print(f)
print(type(f)) # conversion of boolean into complex

f = bool(e) # o/p: True -> bool
print(f)
print(type(f)) # conversion of boolean into boolean


















# float()
# str()
# complex()
# bool()
#


