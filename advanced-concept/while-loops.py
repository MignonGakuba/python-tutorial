
import random


#create variables for to test the while function

playerhp = 260
enemyatkl = 60
enemyatkh = 60



while playerhp > 0 :
    dmg = random.randrange(enemyatkl,enemyatkh)
    playerhp = playerhp -dmg

    if playerhp <= 30:
        playerhp = 30
        print("Enemy strikes for", dmg, "points of damage" , "")

    if playerhp == 30:
        print("You have low health", playerhp, "You have been teleported to the nearest inn")
        break