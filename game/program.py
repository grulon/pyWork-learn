# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:24:07 2017
https://github.com/mikeckennedy/python-for-entrepreneurs-course-demos/blob/master/01-intro-app/program.py
@author: glrulon
"""

from game import Game


def main():
    g = Game()

    while True:
        g.add_move()
        g.show_level()
        if not g.test_player():
            print("Sorry, that was wrong")
            break

    print("Game over")
    print(g.history)

if __name__ == '__main__':
    main()