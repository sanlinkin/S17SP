'''
Created on 12 Apr 2025

@author: Sandeep

Dictionary: Collection of Key-value pairs

dict_name={key1:value1, key2:value2, key3:value3...}

1. Empty dictionary can be created
2. Dictionary doesn't allow duplicates elements
3. Dictionary allows duplicate values but not keys
4. 


'''

d1={}
print(d1)
print(type(d1))

iquest_students={1:'Bhavani', 2:'Chitra', 3: 'Sandeep', 4: 'Sanjana', 5: 'Yogitha'}
print(iquest_students)
print(type(iquest_students))


d2=dict() # creates empty dictionary
print(d2)

d3=dict.fromkeys([1,2,3,4], 'xyz')
print(d3)

iquest_students2={'Bhavani':1,'Chitra':2}
print(iquest_students2)
print(iquest_students2['Chitra'])

d4={1:'Bhavani', 2:'Chitra', 2: 'Chitra'} # Dictionary doesn't allows duplicates.
print(d4)


stds={1:'Bhavani', 2:'Chitra', 3: 'Sandeep', 4: 'Sanjana', 5: 'Yogitha'}
print(stds[3]) # gives the value of 3
print(type(stds)) 

print(stds.keys())
print(stds.values())
  
for ele in stds.values():
    print(ele)
for ele in stds.keys():
    print(ele)

d4={1:'Bhavani', 2:'Chitra', 3: 'Chitra'}  
print(d4)
d4[3]='Sanjana' # modified (3: Chitra) with Sanjana
print(d4)
d4[4]='Yogitha' # adds to the list
print(d4)

d5=d4.copy()
print(d5)

print(d4.items())

print(d4.pop(2)) # remove any element --> 2:chitra & gives the value
print(d4)

print(d4.popitem())
print(d4) # removes only last element --> 4:Yogitha
'''
print(d4.setdefault())
print(d4)
'''
print('d3--->', d3)
print('d4--->', d4)
d4.update(d3)
print('Updated d4', d4)















    
    
    
    
    









