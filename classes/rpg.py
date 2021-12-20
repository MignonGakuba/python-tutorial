import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:

    def __init__(self, hp, atk, df, magic, mp):
        self.maxhp = hp
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_dmg(self):
        return random.randrange(self.atkl, self.atkh)

    def generate_spell_dmg(self, i):
        magicl = self.magic[i]["dmg"] - 5
        magich = self.magic[i]["dmg"] + 5
        return random.randrange(magicl, magich)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_mp(self):
        return self.mp

    def get_max_hp(self):
        return self.maxhp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_mp_cost(self, i):
        # self.mp -=self.magic[i]["cost"]
        return self.magic[i]["cost"]

    def get_spell_name(self, i):
        return self.magic[i]["name"]

