'''
Created on Feb 18, 2020

@author: Chraut
'''

# list
mylist = []
mylist.append(0)
mylist.append(1)
mylist.append(2)

print(mylist[0])
print(mylist[1])
print(mylist[2])

for x in mylist:
    print(x)

mylist = [1,2,3,4,5,6,7,8,9]
print(mylist[8])

# exercise
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("wolrd")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)

