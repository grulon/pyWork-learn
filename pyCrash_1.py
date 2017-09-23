# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 15:50:43 2017

@author: glrulon
"""

#import this

bike = ['heinz57','huffy','Honda','Ducati','harley']

message = 'My first bike was a ' + bike[0].title() + '.'

print(message)

print(bike)

bike.sort() #(reverse=True) reverse causes an error cause Ducati gets popped

popped_bike = bike.pop()

print(bike)
print(popped_bike)

second_bike = bike.pop(1)

msg2 = 'My 2nd bike was a ' + second_bike + '.'

print(msg2)
print(bike)

too_costly = 'Ducati'
bike.remove(too_costly)

print(bike)
bike.append('other')
print(bike)

print(len(bike))