'''
Created on Feb 18, 2020

@author: Chraut
'''
print("hello world")

x = 1

if x == 1:
    print("x is 1")
  
# integer    
myint = 7
print(myint)    

# floats
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
   
# strings   
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

# calculation with numbers and strings
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# declaration of more vaiabels in 1 line
a, b = 3, 4
print(a,b)

# exersice

# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
