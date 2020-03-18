'''
Created on Feb 23, 2020

@author: marbe
'''

# definition of a function
def my_function():
    print("Hello From My Function!")
    
# function with input arguments
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
    
# function with return value
def sum_two_numbers(a, b):
    return a + b

# call a fucntion
# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
print(x) 

# -----------------------------------------------------------------------------------------------------------
# exercise

# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code","More readable code","Easier code reuse","Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(info):
    print("%s is a benefit of functions!" % info)

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()