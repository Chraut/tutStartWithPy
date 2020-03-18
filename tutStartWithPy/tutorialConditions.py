'''
Created on Feb 23, 2020

@author: marbe
'''
# basic conditions
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x != 3) # not equal
print(x < 3) # prints out True


# comarison
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    
    
# in operator

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")

statement = False
another_statement = True
if statement is True:
    # do something
    pass                        # do nothing / when nothing is happen in a method or similar at least the pass statement needs to be filled in
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass  
    
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")
 
# is operator     Unlike the double equals operator "==", the "is" operator does not match the values of the variables, but the instances themselves.
    
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False


# not operator   Using "not" before a boolean expression inverts it.
print(not False) # Prints out True
print((not False) == (False)) # Prints out False



# ------------------------------------------------------------------------------------------------
# Exercise

# change this code
number = 20
second_number = 0
first_array = [True, True, True]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")





