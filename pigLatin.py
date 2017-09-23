# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 15:45:12 2017

@author: glrulon

changed raw_input to input so it would run in python 3
"""

pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():
  print('You typed in: ' + original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print(new_word)
else:
  print('We cannot translate that.')