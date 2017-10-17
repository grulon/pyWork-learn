# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:33:35 2017
 Wizard game  -- talk python training
  
@author: glrulon
"""
from WizActors import Wizard, Creature, Dragon, SmallAnimal
import random
import time


def main():
    print_header()
    game_loop()


def print_header():
    print('-----------------------------------------')    
    print('           WIZARD BATTLE ')    
    print('-----------------------------------------')
    

    
    
def game_loop():
    
    
    creatures = [
                 SmallAnimal('Toad',1),
                 Creature('Tiger',12),
                 SmallAnimal('Bat', 3),
                 Dragon('Dragon', 50, 75, True),
                 Creature('Evil Wizard', 1000),
                 ]
    
    print(creatures)
    
    hero = Wizard('Gandolf', 75)
    
       
    
    
    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from forest...'.format(
              active_creature.name, active_creature.level))
        print()
        
        
        cmd = input('Do you [a]ttack, [r]unaway, or [l]ook around?' )
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard runs and hides taking time to recover...")
                time.sleep(5)
                print("The wizard returns revitalized!")
            
            
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees: '
                  .format(hero.name))
            for c in creatures:
                print('* A {} of level {}'.format(c.name, c.level))
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        else:
            print('Okay, exiting game... bye!')
            break

        print()
        
        
        
if __name__ == '__main__':
    main()
    


