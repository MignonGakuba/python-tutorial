from classes.enemy import Enemy
from classes.rpg import Person

magic = [{"name": "Fire", "cost": 10, "dmg": 60},
         {"name": "Tunder", "cost": 10, "dmg": 80},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


# magic_tunder_name = magic[1]["name"]
# print(magic_tunder_name)

player = Person(460, 65, 60, magic, 34)


