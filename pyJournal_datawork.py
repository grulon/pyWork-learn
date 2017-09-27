# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 10:01:43 2017

Part of pyJournal App

@author: glrulon
"""

import os


def load(name):
    # todo:  populate from file if it exists.
    return []


def save(name, journal_data):
    filename = os.path.abspath(os.path.join('.','journals' , name + '.jrl'))
    print("...... saving to: {}".format(filename))
        
    #fout = open(filename, 'w')  
    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')
        
    #fout.close()  don't need this when WITH is used.
    

def add_entry(text, journal_data):
    journal_data.append(text)


