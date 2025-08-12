import time
import random
import sys

# Introduces the player
print("Welcome to the train...")
print("This train never ends...")
print("With loot...")
print("And with enemies")
name = input("What is your name?: ")
print("Type 'fight' to do damage")

# Easter eggs
if name == "Gumpy":
    print("Hey is that a bom- *BOOM*")
elif name == "Big_brother":
    print("They are always watching...")
elif name == "xXGODSLAYERXx":
    print("MUSHROOMS DIE!")
elif name == "chatGPT":
    print("How did you know it helped me make this?")

# Defines things
health = 100
melee = ["fist", "Dagger", "Sword", "Axe", "twin sword", "twin dagger", "twin axe", "Dark Blade", "Twin Dark Blade", "Triple Dark Blade"]
ranged = ["Bow", "slingshot", "Gun", "Cannon", "Crusafix?", "Soul guitar", "Dual gun"]
magic = ["wand", "Crusafix?", "dual wand", "staff", "dual staff", "hands", "Curse"]
potions = ["Damage", "Mana", "Speed"]
armor = ["leather armor", "wood armor", "chainmail armor", "iron armor", "gold armor", "shattered armor?", "dragon armor", "God armor"]
magic_lvl = 1
damage = 1
ranged_lvl = 1

inv = []

enemies = [
    {
        "tag": "slime",
        "health": 25,
        "damage": 10
    },
    {
        "tag": "rat",
        "health": 5,
        "damage": 1
    },
    {
        "tag": "goblin",
        "health": 50,
        "damage": 25
    },
    {
        "tag": "mummy",
        "health": 75,
        "damage": 50
    },
    {
        "tag": "mirror?",
        "health": 1,
        "damage": 0
    },
    {
        "tag": "orc",
        "health": 200,
        "damage": 100
    },
    {
        "tag": "elf",
        "health": 100,
        "damage": 10
    },
    {
        "tag": "monkey",
        "health": 50,
        "damage": 10
    },
    {
        "tag": "tiger",
        "health": 150,
        "damage": 150
    },
    {
        "tag": "bear",
        "health": 300,
        "damage": 300
    },
    {
        "tag": "zombie",
        "health": 100,
        "damage": 25
    },
    {
        "tag": "demon",
        "health": 250,
        "damage": 100
    }
]

def rand_loot():
    category = random.choice([melee, ranged, magic, potions])
    randloot = random.choice(category)
    print(f"You got a {randloot}!")
    if randloot in melee:
        swap_melee = input(f"Would you like to swap your {inv[0]} for {randloot}? yes or no? ").lower()
        if swap_melee == "yes":
            del inv[0]
            inv.insert(0, randloot)
            if inv[0] == "fist":
                damage = 1
            elif inv[0] == "Dagger":
                damage = 10
            elif inv[0] == "Sword":
                damage = 25
            elif inv[0] == "Axe":
                damage = 30
            elif inv[0] == "twin sword":
                damage = 50
            elif inv[0] == "twin dagger":
                damage = 20
            elif inv[0] == "twin axe":
                damage = 60
            elif inv[0] == "Dark Blade":
                damage = 100
            elif inv[0] == "Twin Dark Blade":
                damage = 200
            elif inv[0] == "Triple Dark Blade":
                damage = 999
        elif swap_melee == "no":
            print(f"You drop the {randloot}!")
    elif randloot in ranged:
        swap_ranged = input(f"Would you like to swap your {inv[1]} for {randloot}? yes or no? ").lower()
        if swap_ranged == "yes":
            del inv[1]
            inv.insert(1, randloot)
            if inv[1] == "Bow":
                ranged_lvl = 30
            elif inv[1] == "slingshot":
                ranged_lvl = 5
            elif inv[1] == "Gun":
                ranged_lvl = 50
            elif inv[1] == "Cannon":
                ranged_lvl = 250
            elif inv[1] == "Crusafix?":
                ranged_lvl = 100
            elif inv[1] == "Soul guitar":
                ranged_lvl = 999
            elif inv[1] == "Dual gun":
                ranged_lvl = 100
        elif swap_ranged == "no":
            print(f"You drop the {randloot}!")
    elif randloot in magic:
        swap_magic = input(f"Would you like to swap your {inv[2]} for {randloot}? yes or no? ").lower()
        if swap_magic == "yes":
            del inv[2]
            inv.insert(2, randloot)
            if inv[2] == "wand":
                magic_lvl = 25
            elif inv[2] == "Crusafix?":
                magic_lvl = 100
            elif inv[2] == "dual wand":
                magic_lvl = 50
            elif inv[2] == "staff":
                magic_lvl = 75
            elif inv[2] == "dual staff":
                magic_lvl = 150
            elif inv[2] == "hands":
                magic_lvl = 1
            elif inv[2] == "Curse":
                magic_lvl = 999
        elif swap_magic == "no":
            print(f"You drop the {randloot}!")
    elif randloot in potions:
        swap_potions = input(f"Whould you like to swap your {inv[3]} for {randloot}? yes or no? ").lower()
        if swap_potions == "yes":
            del inv[3]
            inv.insert(3, randloot)
            if inv[3] == "Damage":
                damage += 50
                ranged_lvl += 50
                magic_lvl += 50
            elif inv[3] == "Mana":
                magic_lvl += 100
            elif inv[3] == "Speed":
                ranged_lvl += 100
        elif swap_potions == "no":
            print(f"You drop the {randloot}!")
    elif randloot in armor:
        swap_armor = input(f"Whould you like to swap your {inv[4]} for {randloot}? yes or no? ").lower()
        if swap_armor == "yes":
            del inv[4]
            inv.insert(4, randloot)
            if inv[4] == "leather armor":
                health += 50
            elif inv[4] == "wood armor":
                health += 100
            elif inv[4] == "chainmail armor":
                health += 150
            elif inv[4] == "iron armor":
                health += 200
            elif inv[4] == "gold armor":
                health += 250
            elif inv[4] == "shattered armor?":
                health += 300
            elif inv[4] == "dragon armor":
                health += 350
            elif inv[4] == "God armor":
                health += 999
        elif swap_armor == "no":
            print(f"You drop the {randloot}!")
    return randloot

def rand_room():
    enemy = random.choice(enemies)
    number = random.randint(1, 5)
    if number > 1:
        enemy_name = enemy['tag'] + 's'
        print(f"There are {number} {enemy_name}!")
    else:
        print(f"There is a lone {enemy['tag']}!")
    return enemy, number

# Starts the game with loot
inv.append(random.choice(melee))
inv.append(random.choice(ranged))
inv.append(random.choice(magic))
inv.append(random.choice(potions))
inv.append(random.choice(armor))
enemy, number = rand_room()

if inv[0] == "fist":
    damage = 1
elif inv[0] == "Dagger":
    damage = 10
elif inv[0] == "Sword":
    damage = 25
elif inv[0] == "Axe":
    damage = 30
elif inv[0] == "twin sword":
    damage = 50
elif inv[0] == "twin dagger":
    damage = 20
elif inv[0] == "twin axe":
    damage = 60
elif inv[0] == "Dark Blade":
    damage = 100
elif inv[0] == "Twin Dark Blade":
    damage = 200
elif inv[0] == "Triple Dark Blade":
    damage = 999
elif inv[1] == "Bow":
    ranged_lvl = 30
elif inv[1] == "slingshot":
    ranged_lvl = 5
elif inv[1] == "Gun":
    ranged_lvl = 50
elif inv[1] == "Cannon":
    ranged_lvl = 250
elif inv[1] == "Crusafix?":
    ranged_lvl = 100
elif inv[1] == "Soul guitar":
    ranged_lvl = 999
elif inv[1] == "Dual gun":
    ranged_lvl = 100
elif inv[2] == "wand":
    magic_lvl = 25
elif inv[2] == "Crusafix?":
    magic_lvl = 100
elif inv[2] == "dual wand":
    magic_lvl = 50
elif inv[2] == "staff":
    magic_lvl = 75
elif inv[2] == "dual staff":
    magic_lvl = 150
elif inv[2] == "hands":
    magic_lvl = 1
elif inv[2] == "Curse":
    magic_lvl = 999
elif inv[3] == "Damage":
    damage += 50
    ranged_lvl += 50
    magic_lvl += 50
elif inv[3] == "Mana":
    magic_lvl += 100
elif inv[3] == "Speed":
    ranged_lvl += 100
elif inv[4] == "leather armor":
    health += 50
elif inv[4] == "wood armor":
    health += 100
elif inv[4] == "chainmail armor":
    health += 150
elif inv[4] == "iron armor":
    health += 200
elif inv[4] == "gold armor":
    health += 250
elif inv[4] == "shattered armor?":
    health += 300
elif inv[4] == "dragon armor":
    health += 350
elif inv[4] == "God armor":
    health += 999

# While True loop
while True:
    cmd = input(f"{name}: ")

    if cmd == "inv":
        print(inv)

    if cmd == "fight":
        enemy['health'] -= damage + magic_lvl + ranged_lvl
        print(f"It has {enemy['health']} health left!")
        if enemy['health'] > 0:
            health -= enemy['damage'] * number
            print(f"You have {health} health left!")

    if enemy['health'] < 1:
        print("You killed it!")
        if inv[4] == "leather armor":
            health = 50
        elif inv[4] == "wood armor":
            health = 100
        elif inv[4] == "chainmail armor":
            health = 150
        elif inv[4] == "iron armor":
            health = 200
        elif inv[4] == "gold armor":
            health = 250
        elif inv[4] == "shattered armor?":
            health = 300
        elif inv[4] == "dragon armor":
            health = 350
        elif inv[4] == "God armor":
            health = 999
        randloot = rand_loot()
        enemy, number = rand_room()

    if health < 1:
        print(f"You died to {enemy['tag']}!")
        time.sleep(3)
        sys.exit()

    if enemy['tag'] == "mirror?" and enemy['health'] < 1 and inv[1] == "Crusafix?" and inv[2] == "Crusafix?":
        del inv[2]
        inv.insert(2, "Curse")
        print("A curse has been given to you...")

    if cmd == "help":
        print("Commands:")
        print("- fight: attack the enemy")
        print("- inv: show your inventory")
        print("- help: show this help menu")



    
