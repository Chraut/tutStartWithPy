'''
Created on Feb 23, 2020

@author: marbe
'''
# argument specifier
name = "John"
print("Hello, %s!" % name)

# more then one specifier
name = "John"
age = 12
print("%s is %d years old" % (name, age))

name = "John"
age = "twelve"
print("%s is %s years old" % (name, age))

# Print list -> any object can be specified with %s

list = [1,2,3,4,5,6]
print("This is my list %s" % list)

# Exercise

data = ("John", "Doe", 53.44)
format_string = "Hello"

print("%s %s %s. Your current balance is $%s" % (format_string, data[0], data[1], data[2]))

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)