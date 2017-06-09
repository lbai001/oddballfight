# pylint: disable=invalid-name, line-too-long
"""This script is the flow control script for OddballFight, alerts user what action to take after an action has been completed"""
import re
from Game import Game


def start():
    new_game = Game()
    start_confirm = raw_input(
        "Welcome to Oddball Fight! Do you wish to start? y/n : ")
    p = re.compile('^Y|y|O|o')
    match = p.match(start_confirm)
    while match:
        new_game.start_game("user")
        new_game.choose_opponent("opponent")
        while not new_game.end_fight:
            if new_game.current_opponent and new_game.current_opponent:
                new_game.start_fight()
                new_game.end_fight = True
            else:
                new_game.choose_opponent("opponent")
    else:
        print 'game ended'


if __name__ == '__main__':
    start()
