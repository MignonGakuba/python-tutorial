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

# Create  some items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
high_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP?MP of one party member", 9999)
hi_elixer = Item("High Elixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damge", 500)

# Create list of items and magic
player_magic = [fire, thunder, blizzard, meteor, cure, cura]
payer_items = [{"item": potion, "quantity": 5}, {"item": high_potion, "quantity": 5},
               {"item": super_potion, "quantity": 5}, {"item": elixer, "quantity": 5},
               {"item": hi_elixer, "quantity": 2}, {"item": grenade, "quantity": 5}]

# Objects: player, enemy are to instantiate of the class Person
player = Person("Valos:", 3260, 132, 60, 34, player_magic, payer_items)
player2 = Person("Nick:", 4160, 188, 60, 34, player_magic, payer_items)
player3 = Person("Robot:", 3089, 174, 60, 34, player_magic, payer_items)

players = [player, player2, player3]
enemy = Person("", 1200, 701, 45, 25, [], [])

running = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:

    print("=======================")

    print("\n\n")
    print(" NAME                  HP                                  MP")
    for player in players:
        player.get_stats()

    print("\n")

    for player in players:
        player.choose_action()
        choice = input("Choose action: ")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_dmg()
            enemy.take_damage(dmg)
            print("You attack for ", dmg, "points of damage.   Enemy HP:", enemy.get_hp())

        elif index == 1:
            player.choose_magic()
            choice_magic = int(input("Choose magic: ")) - 1

            if choice_magic == -1:
                continue

            spell = player.magic[choice_magic]
            magic_dmg = spell.generate_dmg()

            current_mp = player.get_mp()

            if spell.cost > current_mp:
                print(bcolors.FAIL + "\nNot enough MP\n" + bcolors.ENDC)
                continue

            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " heals for ", str(magic_dmg), "HP" + bcolors.ENDC)
            elif spell.type == "black":
                enemy.take_damage(magic_dmg)
                print(bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + bcolors.ENDC)

        elif index == 2:
            player.choose_item()
            item_choice = int(input("Choose items: ")) - 1

            if item_choice == -1:
                continue

            item = player.items[item_choice]
            player.items[item_choice]["quantity"] -= 1

            if player.items[item_choice]["quantity"] == 0:
                print(bcolors.FAIL + "\n" + "None left..." + bcolors.ENDC)
                continue

            if item["item"].type == "potion":
                player.heal(item.prop)
                print(bcolors.OKGREEN + "\n" + item["item"].name + "heals for", str(item["item"].prop),
                      "HP" + bcolors.ENDC)

            elif item["item"].type == "elixer":
                player.hp = player.max_hp
                player.mp = player.max_mp
                print(bcolors.OKGREEN + "\n" + item["item"].name + "fully restores HP/MP " + bcolors.ENDC)

            elif item["item"].type == "attack":
                enemy.take_damage(item.prop)
                print(bcolors.FAIL + "\n" + item["item"].name + "deals ", item["item"].prop,
                      "points of damage" + bcolors.ENDC)

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
