import random


class Enemy:
    atkl = 60
    atkh = 80

    def getAtkl(self):
        print(self.atkl)
        # return self.atkl

    def getAtkh(self):
        print(self.atkh)
        # return self.atkh


enemy1 = Enemy()
dmg = enemy1.getAtkh()
print(dmg)

...
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage", "Current HP is",playerhp)

    if playerhp > 30:
        continue

    print("You have low health:", playerhp, "You have been teleported to the nearest inn")
    break
    # if playerhp == 30:
    #     print("You have low health: ", playerhp, "You have been teleported to the nearest inn")
    #     break
