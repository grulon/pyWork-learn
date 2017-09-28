# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 14:35:27 2017

@author: glrulon
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