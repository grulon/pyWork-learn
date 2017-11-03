# -*- coding: utf-8 -*-
"""
Statistics standin for python 2

Created on Fri Nov  3 08:53:05 2017

@author: glrulon
"""

def mean(data):

    total = 0.0
    count = 0
    for x in data:
        count += 1
        total += x
        
    return total / max(1,count)