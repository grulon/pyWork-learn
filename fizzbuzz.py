# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:35:27 2017

@author: glrulon


## fun stuff to do...
1) improve function... make slicker
2) return in a list/array
3) return as dict, with counter in index.
"""

def fizzbuzz(start,end):
    for x in range (start,end):      
        if x % 3 == 0 and x % 5 == 0:           
            print('FizzBuzz')       
        elif x % 3 == 0:            
            print('Fizz')       
        elif x % 5 == 0:            
            print ('Buzz')      
        else:           
            print (x)

    
    
fizzbuzz(91,100)