# -*- coding: utf-8 -*-
"""
concept Dictionary

Created on Thu Nov  2 15:06:31 2017

@author: glrulon
"""

lookup = {}

lookup = dict()
lookup['age'] = 46
lookup['loc'] = 'Indiana'

lookup = {'age':46, 'loc':'Indiana'}
lookup = dict(age=46, loc='Indiana')


class Wizard:
    def __init__(self, name, level):
        self.level = level
        self.name = name
        
gandolf = Wizard("Gandolf", 46)

print(gandolf.__dict__)



home = lookup['loc']
print('home:' + home)

print(lookup)

print(lookup['loc'])

lookup['cat'] = 'Fun code demos'

if 'cat' in lookup:
    print(lookup['cat'])

    
    
# Suppose these came from a data source (web service, database, etc)
# we want to randomly access
import collections

User = collections.namedtuple('User', 'id, name, email')

users = [
    User(1, 'user1', 'user1@email.com'),
    User(2, 'user2','user2@email.com'),
    User(3, 'user3', 'user3@email.com'),
    User(4, 'user4', 'user4@email.com'),
]    

lookup = dict()
for u in users:
    lookup[u.id] = u #can use any col as key: id, name, email...

print(lookup[3])    
    
    
    
    
    
    
# lambdas are small inline methods

def find_significant_nums(nums, predicate):
    for n in nums:
        if predicate(n):
            yield n
            
numbers = [1,1,2,3,5,8,13,21,34]  #fibo nums
sig = find_significant_nums(numbers, lambda x: x % 2 == 1)  # looking for odd numbers
print(type(sig))

for x in sig:
    print(x)






            
            
    
    
    
    