# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:24:21 2017
https://github.com/mikeckennedy/python-for-entrepreneurs-course-demos/blob/master/01-intro-app/game.py
@author: glrulon
"""

import os
import random
import time
import colorama

import sys


class Game:
    def __init__(self):
        self.history = []
        self.plays = [
            (colorama.Fore.RED + 'Red', 'r'),
            (colorama.Fore.YELLOW + 'Yellow', 'y'),
            (colorama.Fore.GREEN + 'Green', 'g'),
            (colorama.Fore.CYAN + 'Blue', 'b')
        ]

    def show_level(self):
        self.clear()
        for h in self.history:
            print(h[0], end='  ')
            sys.stdout.flush()
            time.sleep(1)

        self.clear()

    def add_move(self):
        self.history.append(random.choice(self.plays))

    def test_player(self):
        print(colorama.Fore.WHITE + "{} moves:".format(len(self.history)))
        for t, v in self.history:
            guess = input("Next [r,g,b,y]: ")
            if guess != v:
                return False

        return True

    # noinspection PyMethodMayBeStatic
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')