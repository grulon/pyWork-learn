# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 09:02:21 2017

@author: glrulon
"""
import random

class Wizard:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
              self.name, creature.name))
        
        my_roll = random.randint(1, 12) * self.level
        creature_roll = Creature.get_defensive_roll(creature) #random.randint(1, 12) * creature.level

        print("I roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))
       
        if my_roll >= creature_roll:
            print("The wizard has triumphed over {}".format(creature.name))
            return True
        else:
            print("The wizard has been DEFEATED!!!")
            return False
        
class Creature:
    def __init__(self, name, the_level):
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature: {} of level {}".format(
            self.name, self.level)
        
    def get_defensive_roll(self):
        return random.randint(1,12) * self.level


class Dragon(Creature):
    def __init__(self, name, level, scale_thickness):
        super().__init__(name, level)
        self.scale_thickness = scale_thickness
        