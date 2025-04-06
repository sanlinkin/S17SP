'''
Created on 27 Mar 2025

@author: Dell

Operator: A symbol which performs operation on operands (variables)
Basic classification:Classification based on operands:
1. Unary Operator: performs operation on single operand/variable
2. Binary Operator: performs operation on two operands/variable
3. Ternary Operator: performs operation on three operands/variable

Classification based on operations: (types of Operators)
1. Assignment Operator: =
2. Arithmetic Operators: +, -, *, /, %(moduls), **(exponent), //(Integer division)
3. Relational/Comparsion Operators: >, <, ==,1=, <=, >=
4. Logical Operators: AND, OR, NOT
5. Membership Operators: in, not in
6. Identity operators: is, is not
7. Unary minus operator: -

'''
print('====Arithmetic Operators====')
a=20
b=20
c=a+b
print(f"addtition of {a} and {b}:", c)
print(f"difference b/w {a} and {b}:", a-b)
print(f"multiplication of {a} and{b}:", a*b)
print(f"division of {a} and {b}:", a/b)
print(f"modulus of {a} and {b}:", a%b)
print(f"integer division of {a} and {b}:", a/b)
print(f"sqaure of {a} :", a**2)

print("=====Relational/Comparision Operators======")
print(f"is {a} greater than {b}", a>b)
print(f"is {a} lesser than {b}", a<b)
print(f"is {a} equal to {b}", a==b)

print("=====Logical Operators======")

print('=======AND operators======')
print(True and False)
print(False and True)
print(False and False)
print(True and True)

print("====oR operators=====")
print(True or False)
print(False or True)
print(False or False)
print(True or True)

print("===NOT operators=====")
print(not True)
print(not False)

print("=======Membership Operators========")
print("A" in "alphabet") 
"upper or lower case  through error/false"
print("i" in "alphabet")
print("i" not in "alphabet")

print("=====Identity Operators========")
print(a is b)
print("neymar" is "Neymar")
d='vivek'
e='Vivek'
print(d is e)
print(id(a))
print(id(b))
print(id(d))
print(id(e))






