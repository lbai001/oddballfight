# pylint: disable=invalid-name, line-too-long, too-many-instance-attributes, too-few-public-methods
"""This class is the base character class of every created charactor"""


class Character:
    """basic prototype of a character"""

    def __init__(self, name, hp, mp, charclass):
        """Initializes the data."""

        self.name = name
        self.level = 0
        self.hp = self.level + hp
        self.mp = int(self.hp * 0.8)
        self.char_class = charclass
        self.inventory = []
        self.exp = 0
        self.exp_cap = 20 + self.level * 5
        self.score = 0

    def show_stats(self):
        """prints character stats to the ternimal"""

        print "name: {}".format(self.name)
        print "level: {}".format(self.level)
        print "hp: {}".format(self.hp)
        print "mp: {}".format(self.mp)
        print "class: {}".format(self.char_class)
        print "score: {}".format(self.score)

    def show_skill_names(self, skills):
        """prints skill names in an array"""
        result = []
        for item in skills:
            result.append(item.items()[0][1])
        return result

    def store_item(self, item):
        """put an item into inventory"""
        self.inventory.append(item)

    def delete_item(self, index):
        """deletes an item from inventory"""
        del self.inventory[index]

    def delete_then_store(self, item):
        s = raw_input(
            "which item do you want to delete? enter number : ")
        self.delete_item(int(s) - 1)
        self.store_item(item)
        print "item deleted, {} stored in your inventory".format(item["name"])


class Travis(Character):
    """Initializes Travis."""

    def __init__(self, name, hp, mp, charclass):
        Character.__init__(self, name, hp, mp, charclass)
        self.char_class = charclass
        self.weapon = {"name": "stick", "dmg": 1}
        self.skills = [{"name": "Attack", "dmg": self.weapon["dmg"] + self.level, "mpc": 0}, {
            "name": "Poke", "dmg": self.level + 2, "mpc": 2}, {"name": "OpenRA", "dmg": self.level + 4, "mpc": 4}]
        self.skill_n = self.show_skill_names(self.skills)

    def show_skills(self):
        print "skills : {}".format(self.skill_n)

    def show_inventory(self):
        print "inventory : {}".format(self.inventory)

    def show_euipment(self):
        print "euipped: {}".format(self.weapon["name"])


class Rob(Character):
    """Initializes Rob"""

    def __init__(self, name, hp, mp, charclass):
        Character.__init__(self, name, hp, mp, charclass)
        self.char_class = charclass
        self.weapon = {"name": "nerdy wand", "dmg": 1}
        self.skills = [{"name": "Attack", "dmg": self.weapon["dmg"] + self.level, "mpc": 0}, {
            "name": "Nerdy Glare", "dmg": self.level + 3, "mpc": 2}, {"name": "Nerd Hand Gastures", "dmg": self.level + 5, "mpc": 4}]
        self.skill_n = self.show_skill_names(self.skills)

    def show_skills(self):
        print "skills : {}" .format(self.skill_n)

    def show_inventory(self):
        print "inventory : {}".format(self.inventory)

    def show_euipment(self):
        print "euipped: {}".format(self.weapon["name"])


class XiaoLu(Character):
    """Initializes XiaoLu"""

    def __init__(self, name, hp, mp, charclass):
        Character.__init__(self, name, hp, mp, charclass)
        self.char_class = charclass
        self.weapon = {"name": "redbull can", "dmg": 300}
        self.skills = [
            {"name": "Attack", "dmg": self.weapon["dmg"] + self.level, "mpc": 1}]
        self.skill_n = self.show_skill_names(self.skills)

    def show_skills(self):
        print "skills : {}" .format(self.skill_n)

    def show_inventory(self):
        print "inventory : {}".format(self.inventory)

    def show_euipment(self):
        print "euipped: {}".format(self.weapon["name"])
