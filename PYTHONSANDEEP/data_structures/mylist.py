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
    3. set {}
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
3. Accessing elements
    - Indexing/ Using index (starts from 0)
        > positive (starts from left to right)
        > negetive (starts from right to left)
    - Using slicing operator  
4. list can be modified
    Using slicing operator  list_name[start : stop : step] -> takes index as input default values:
      start: index 0
      stop: last index
      step: 
5. List stores 
6.
7.
8.

Example execise: Creating the list of squares of odd numbers
Given list
empty list
list2=[]
1. Fetch each element from the given list--> while/for loop
2. Check whether the element is odd --> if ele%2==1
3. If the element is odd get the square of it--> x*ele**2
4. append the result of step 3 to an new list (Create a empty list before step 1)--> list2.append
5. Repeat step 1 to 4 for all elements
6. Print the new list created from the above process. print(list2)

'''
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

'''
#c={1:"vivek"}
#print(c)
'''
d=list(range(1, 20))
print(d)

# Accessing the elements using index - use only square brackets []
print(c[3])
print(c[-1])

# Modification/replacement using index
c[1]="vivek" # re-initialization 
print(c)


# slicing operator: list_name[start : stop : step] -> index

print('d[::]-->', d[::])
print('d[3:9]-->', d[3:9])
print('d[:12', d[:12])
print('d[[6:]', d[6:])
print('d[-12:-6]-->', d[-12:-6])
print('d[::2]', d[::2])
print('d[::-1]', d[::-1])

print('d[-12:-6:-1]-->', d[-12:-6:-1])

# Accessing using loops
print('c-->', c)
# for loop:
print("====for loop====")
for ele in c:
    print(ele)
'''
'''
print("===while loop===")
i=0
while i<5:
    print(c[i])
    i+=1
'''
'''   
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])

'''
'''
i=0
while i<len(d):
    print(d[i])
    i+=1  
       
# Finding the length of a collection
print(len(c)) 

# print odd number in list(d)
for n in d:
    if n%2 ==1:
        print(n)
'''   
'''    
# print word which contains 'a' in list(e)       
e=["Bhavani", "Chitra", "Sandeep", "Sanjana", "Yogitha"]
for g in e:
    if 'a' in g:
        print(g)  
'''
'''
e=["Bhavani", "Chitra", "Sandeep", "Sanjana", "Yogitha", None, "Bhavani"]
print(e)  
'''
'''
e.append("Manju")
print(e)
        
e.insert(5, "iQuest")    
print(e)  

e.append(c) 
print(e)   
        
'''
'''
# list of squares for odd numbers:
a=[]
print(type(a))

y=[15,30,45,22,10,60,13]
for n in y:
    if n%2==1:
        #print(n**2)
        a.append(n**2)
print(a)
'''
# copy list   
'''   
f=e.copy()
print(f)

print(e.count("Bhavani"))

# extend 
e.extend(c)
print('e.extend(c):', e)

#'check length of c'
#print(len(e))
#print(e[10])
#print(e[11])

# index
#e.index(value, start, stop)
print(e.index(4.76))
print('e.count("Bhavani"):',e.count("Bhavani"))
print('e.count("Bhavani"):',e.index("Bhavani", 1))

'''
'''
 Q. Find the indices of a element present in the list

'''
'''
print('c-->', c)
print(c.pop(2))
print(c)
print(c.remove(True))
print(c)
print(c.remove("vivek"))
print(c)
print('c.pop()', c.pop())
print(c)
c.remove(True)
print(c)

'''
''' 
26/04/2025
'''

even_list=[]
for i in range(1,25):
    if i%2==0:
        #print(i)
        even_list.append(i) # add element to the list
print(even_list)
        
#List comprehension
even_list_comp={i for i in range(1,25) if i%2==0}
print("even_list_comp", even_list_comp)



        
        





