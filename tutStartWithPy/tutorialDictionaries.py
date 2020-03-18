'''
Created on Feb 23, 2020

@author: marbe
'''

# create a dictionary
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# or (is the same)
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

# iteration of a dictionary
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
# remove a vuel in teh dictionray
del phonebook["John"]
print(phonebook)

# or (the same)
phonebook.pop("Jill")
print(phonebook)

# ----------------------------------------------------------------------------------------------
# exercise

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

# write your code here
phonebook["Jake"] = 938273443
phonebook.pop("Jill")


# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")