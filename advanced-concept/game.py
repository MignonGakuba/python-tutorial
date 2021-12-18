

'''
    Pogram: Tutorial folass
    Author: Mignon G
    Copyright: 2021

'''
import random


class Enemy:

    #Create variable in the class Enemy

    hp = 200
    # Create a constructor with the variables atkl atkh
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtkl(self):
        print(self.atkl)
        # return self.atkl

    def getAtkh(self):
        print(self.atkh)
        # return self.atkh

    def getHp(self):
        print("HP is ", self.hp)


enemy1 = Enemy(40,50)
enemy1.getAtkh()
enemy1.getHp()

enemy2 = Enemy(20,30)
enemy1.getAtkl()

...
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage", "Current HP is", playerhp)

    if playerhp > 30:
        continue

    print("You have low health:", playerhp, "You have been teleported to the nearest inn")
    break
    # if playerhp == 30:
    #     print("You have low health: ", playerhp, "You have been teleported to the nearest inn")
    #     break
