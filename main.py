from classes.rpg import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item


# Create Black magic
fire = Spell("Fire", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
quake = Spell("Quake", 14, 140, "black")
meteor = Spell("Meteor", 20, 200, "black")

# Create White magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# Create Item
potion = Item("Potion","potion","Heals 50 HP",50)
high_potion = Item("Hi-Potion","potion","Heals 100 HP",100)
super_potion = Item("Super Potion","potion","Heals 250 HP",150)



# Objects: player, enemy are the instantiate of the class Person
player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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

        spell = player.magic[choice_magic]
        magic_dmg = spell.generate_dmg()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
            continue
        player.reduce_mp(spell.cost)

        if spell.type == "white":
            player.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "heals for ", str(magic_dmg), "HP" + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + "deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

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
