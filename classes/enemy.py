

''''
    Create class to import in the main
'''
class Enemy:

    def __init__(self, hp ,atkl, atkh,mp):
        self.hp = hp
        self.atkl = atkl
        self.atkh = atkh
        self.mp = mp

    def get_hp(self):
        return self.hp


    def get_mp(self):
        return self.mp

    def get_atkl(self):
        return self.atkl

    def get_atkh(self):
        return self.atkh