'''
Created on Feb 23, 2020

@author: marbe
'''
# Python follows the order of operation
number = 1 + 2 * 3 / 4.0
print(number)

remainder = 11 % 3
print(remainder)

# power relationship
squared = 7 ** 2
cubed = 2 ** 3

print(squared)
print(cubed)

# string concatenating "addition"
helloworld = "hello" + " " + "world"
print(helloworld)

# Using operators with lists
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers;
print(all_numbers)

print([1,2,3] * 3)

# Exercise

x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = [x]*10 + [y]*10
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")