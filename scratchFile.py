# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 10:05:58 2017

@author: glrulon
"""

def hello():
    print("Hello world!")
    print(100 < 101 or 1==2)
    

def cube(number):
  return number ** 3

def by_three(number):
  if number % 3 == 0:
    return cube(number)
  else:
    return False    
    
  hello()
 
one = by_three(9)
two = by_three(10)   

print(one)
print(two)

