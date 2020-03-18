'''
Created on Feb 23, 2020

@author: marbe
'''
# module ends with .py

import urllib
dir(urllib)

import re

# Your code goes here
find_members = []
for member in dir(re):
    if "find" in member:
        find_members.append(member)

print(sorted(find_members))