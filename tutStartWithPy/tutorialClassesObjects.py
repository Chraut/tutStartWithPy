'''
Created on Feb 23, 2020

@author: marbe
'''

# definition of a class
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

# assign a class to an object
myobjectx = MyClass()

# call a function inside a object
myobjectx.function()

# call a variable of an object
print(myobjectx.variable)

# more then 1 object and change of variable

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.variable = "yackity"

# Then print out both values
print(myobjectx.variable)
print(myobjecty.variable)

# ----------------------------------------------------------------------------------------------------------
# exercise

# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car2 = Vehicle()

car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.0
car1.name = "Fer"
car2.color = "blue"
car2.kind = "van"
car2.name = "Jump"
car2.value = 10000.0


# test code
print(car1.description())
print(car2.description())