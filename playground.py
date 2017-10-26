# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:37:30 2017

@author: glrulon

 5! = 120
 5 * 4 * 3 * 2 * 1

 Recursion

"""

def factorial(n):
    if n <= 1:
        return 1
        
    return n * factorial(n-1)


print("5!={:,}, 3!={:,}, 11!={:,}".format(
    factorial(5),
    factorial(3),
    factorial(11)
))
