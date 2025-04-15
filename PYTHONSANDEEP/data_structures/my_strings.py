'''
Created on 14 Apr 2025

@author: Sandeep

Strings: word/ phrase/ sentence/ paragraph

Letters: Characters in python 

Def: string is a character/ collection of characters

Leading spaces: space at the beginning
Trailing spaces: space at the end 
'''
name = ' Vivek Nagaraju ' #leading spaces

print('name:', name)
print(type(name))
nick_name=''

print("nick_name:", nick_name)
print(type(nick_name))

age = 35 # "35" consider as string
print("age:", age)
print(type(age))

#Access using index
print(name[0]) 

#Access using for loop
print("====Access using for loop====")
for letter in name:
    print(letter)
    
#Access using slicing operator
print("===Access using slicing operator===")
print(name[1:4])
print(type(name[1:4]))
    
address="""iQuest, 
Hebbal Industrial Area,
Mysuru.
"""   
print(address)

#Modification: immutable/ cannot modify
#print(name)# type error: string object does not support item assignment

modified_name=name.replace('v','z') 
print('name:', name)
print("modified_name:", modified_name)

#capitalize()
print("capitalize with leading space:", name.capitalize())

print(name.strip().capitalize())
#name.rstrip()
#name.lstrip()

print(address.casefold()) #converts upper cases to lower cases

print(name.upper()) # converts lower to upper cases

print(name.count('v'))

print(name.find('z'))

#print(name.index('z')) # raises value error when substring is not found.

print(name.isalnum())
print(name.casefold())
print(name.lower())

print(name.split())

name_list=["My", "Name", "is", "vivek"]
name_sentence=' '.join(name_list)
print(name_sentence)

print(len(name))

print(name.isalpha())

print(name.isnumeric())

print(name.isalnum())







