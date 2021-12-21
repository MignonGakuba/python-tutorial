from classes.enemy import Enemy
from classes.rpg import Person, bcolors
from classes.magic import Spell

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Tunder", "cost": 10, "dmg": 120},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


#Create Black magic

fire = Spell("Fire", 10, 100, "black")
blizzard = Spell("Blizzard", 10,100,"black")
thunder = Spell("Thunder", 10, 120,"black")
quake = Spell("Quake", 10, 130,"black")
meteor = Spell("Meteor", 10,130,"black")

player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:

    print("=======================")
    player.choose_action()
    choice = input("Choose action: ")
    index = int(choice) - 1

    print("You choice", index)

    if index == 0:
        dmg = player.generate_dmg()
        enemy.take_damage(dmg)
        print("You attack for ", dmg, "points of damage.   Enemy HP:", enemy.get_hp())

    elif index == 1:
        player.choose_magic()
        choice_magic = int(input("Choose magic: ")) - 1
        magic_dmg = player.generate_spell_dmg(choice_magic)
        spell = player.get_spell_name(choice_magic)
        cost = player.get_spell_mp_cost(choice_magic)

        current_mp = player.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue

        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_dmg()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "points of damage.")

    print("________________________________")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)

    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "YOU WIN" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + "You enemy has defeated you!" + bcolors.ENDC)
        running = False
