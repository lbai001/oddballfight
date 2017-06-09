# pylint: disable=invalid-name, line-too-long
import re
from lib.Character import *
from lib.Fight import *
import random


class Game:
    def __init__(self):
        self.xiaolu = XiaoLu("xiaolu", 200, 300, "GM")
        self.rob = Rob("rob", 15, 15, "Nerd")
        self.travis = Travis("travis", 20, 10, "Business Man")
        self.current_user = ""
        self.current_user_s = ""
        self.current_opponent_s = ""
        self.current_opponent = ""
        self.possible_opponent = ['xiaolu', 'travis', 'rob']
        self.end_fight = False
        self.first_time = True

    def choose_opponent(self, player):
        choose = raw_input(
            "who do you wish to fight? {}: ".format(self.possible_opponent))
        if choose in self.possible_opponent:
            self.current_opponent = choose
            self.confirm_opponent(player)
        else:
            print "you cant choose that player as opponent"

    def confirm_opponent(self, player):
        self.set_user_stat()
        # print self.current_opponent_s.__dict__

        self.current_opponent_s.show_stats()
        self.current_opponent_s.show_skills()
        self.current_opponent_s.show_euipment()
        s = raw_input(
            "are you sure you want to fight {}? y/n :".format(self.current_opponent))
        p = re.compile('^Y|y|O|o')
        match = p.match(s)
        if match:
            print "Fight Start {} VS {}".format(self.current_user, self.current_opponent)
            self.first_time = False
        else:
            self.choose_opponent(player)

    def start_fight(self):
        fight = Fight(user=self.current_user_s,
                      opponent=self.current_opponent_s, user_mp=self.current_user_s.mp, opp_mp=self.current_opponent_s.mp)
        fight.start_fight()

    def set_user_stat(self):
        all_char = [XiaoLu("xiaolu", 200, 300, "GM"), Rob(
            "rob", 15, 15, "Nerd"), Travis("travis", 20, 10, "Business Man")]
        for item in all_char:
            if self.first_time:
                if item.name == self.current_user:
                    self.current_user_s = item
                elif item.name == self.current_opponent:
                    self.current_opponent_s = item
            else:
                if self.current_user_s.name == item.name:
                    item.exp = self.current_user_s.exp
                    item.score = self.current_user_s.score
                    item.level = self.current_user_s.level
                    item.weapon = self.current_user_s.weapon
                    item.inventory = self.current_user_s.inventory
                    self.current_user_s = item
                    self.current_user_s.exp_cap += item.exp_cap * self.current_user_s.level
                    self.current_user_s.hp += self.current_user_s.level
                    self.increase_attack_damage(self.current_user_s)
                elif self.current_opponent_s.name == item.name:
                    item.level = self.current_opponent_s.level
                    item.score = self.current_opponent_s.score
                    self.current_opponent_s = item
                    self.current_opponent_s.hp += int(
                        self.current_opponent_s.level * 1.5)
                    self.increase_attack_damage(self.current_opponent_s)

    def increase_attack_damage(self, player):
        for index, item in enumerate(player.skills):
            if player.skills[index]["name"] == "Attack":
                player.skills[index]['dmg'] += player.level + \
                    player.weapon['dmg']
            else:
                player.skills[index]['dmg'] += player.level

    def set_opponent(self, s):
        opponents = ['xiaolu', 'travis', 'rob']
        index = opponents.index(s)
        possible_opponent = opponents[0:index:] + \
            opponents[index + 1::]
        self.possible_opponent = possible_opponent

    def start_game(self, player):
        if self.first_time:
            s = raw_input("Who are you? : ")
            if len(s) and s == "travis":
                self.current_user = "travis"
                self.current_user_s = self.travis
                self.travis.show_stats()
                self.travis.show_skills()
                self.travis.show_inventory()
                self.travis.show_euipment()
                print "you are now {}".format(s)
                self.set_opponent(s)

            elif len(s) and s == "rob":
                self.current_user_s = self.rob
                self.current_user = "rob"
                self.rob.show_stats()
                self.rob.show_skills()
                self.rob.show_inventory()
                self.rob.show_euipment()
                print "you are now {}".format(s)
                self.set_opponent(s)

            elif len(s) and s == "xiaolu":
                self.current_user_s = self.xiaolu
                self.current_user = "xiaolu"
                self.xiaolu.show_stats()
                self.xiaolu.show_skills()
                self.xiaolu.show_inventory()
                self.xiaolu.show_euipment()
                print "you are now {}".format(s)
                self.set_opponent(s)

            else:
                print "you are not one of oddball yet!"
        else:
            self.set_user_stat()
            # print self.current_user_s.__dict__
            self.end_fight = False
