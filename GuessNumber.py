# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 12:31:59 2017

@author: glrulon
"""

#Guess the number App from Talk Python lesson#2 
import random

print('----------------------------')
print('   GUESS THAT NUMBER GAME  ')
print('----------------------------')

the_number = random.randint(0, 100)
guess = -1
name = input('What is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number :
        print('Your guess of ' + str(guess) +' was too low!')
    elif guess > the_number:
        print('try again, {1}!  Your guess of {0} was too high'.format(guess,name))
    else:
        print('Great job, {0}!!! You win it was {1}!'.format(name, guess))

print('done')
