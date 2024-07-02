import random
from cave import Cave
from character import Enemy, Friend, Bystander
from item import Item


#Places
pleasant_park = Cave("Pleasant Park")
pleasant_park.set_description("A popular landing spot with many houses and loot.")

tilted_towers = Cave("Tilted Towers")
tilted_towers.set_description("A bustling area with tall buildings and high risk.")

salty_springs = Cave("Salty Springs")
salty_springs.set_description("A suburban area with several houses and tight spaces.")

weeping_woods = Cave("Weeping Woods")
weeping_woods.set_description("A dense forest with plenty of trees and hiding spots.")

loot_lake = Cave("Loot Lake")
loot_lake.set_description("A serene lake with a house in the middle and lots of loot.")

flush_factory = Cave("Flush Factory")
flush_factory.set_description("An abandoned toilet factory with scattered loot.")

spawn_island = Cave("Spawn Island")
spawn_island.set_description("A small island with minimal resources but strategic location.")

shifty_shafts = Cave("Shifty Shafts")
shifty_shafts.set_description("An old mining area with plenty of hiding spots and tunnels.")

#Links
salty_springs.link_cave(tilted_towers, "west")
salty_springs.link_cave(pleasant_park, "north")

pleasant_park.link_cave(salty_springs, "south")
tilted_towers.link_cave(salty_springs, "east")
pleasant_park.link_cave(weeping_woods, "east")
weeping_woods.link_cave(loot_lake, "south")
flush_factory.link_cave(loot_lake, "north")
loot_lake.link_cave(flush_factory, "south")
weeping_woods.link_cave(spawn_island, "east")
spawn_island.link_cave(shifty_shafts, "north")
shifty_shafts.link_cave(spawn_island, "south")
spawn_island.link_cave(weeping_woods, "west")
loot_lake.link_cave(weeping_woods, "north")
weeping_woods.link_cave(pleasant_park, "west")
salty_springs.link_cave(loot_lake, "east")
loot_lake.link_cave(salty_springs, "west")
pleasant_park.link_cave(weeping_woods, "east")


#Characters
storm_king = Enemy("Storm King", "A monstrous entity with immense power")
storm_king.set_conversation("You cannot escape the storm!")
storm_king.set_weakness("Rocket Launcher")
storm_king.set_health(100)

jonesy = Friend("Jonesy", "A reliable teammate")
jonesy.set_conversation("Stay close and we'll survive. Take this Rocket Launcher to help yourself out against Storm.")
jonesy.set_health(100)

midas = Enemy("Midas", "A cunning leader with a golden touch")
midas.set_conversation("Everything I touch turns to gold!")
midas.set_weakness("Shadow Bomb")
midas.set_health(80)

brutus = Bystander("Brutus", "A heavily muscled agent")
brutus.set_conversation("Keep your head down and stay alert.")

meowscles = Enemy("Meowscles", "A muscular cat with a fierce attitude")
meowscles.set_conversation("You're in my sights!")
meowscles.set_weakness("Minigun")
meowscles.set_health(90)

sky = Enemy("Sky", "A fearless adventurer")
sky.set_conversation("Let's see what you've got!")
sky.set_weakness("Boom Bow")
sky.set_health(85)

peely = Friend("Peely", "A lovable banana")
peely.set_conversation("I'm ripe and ready!")
peely.set_health(100)

#Set characters
salty_springs.set_character(storm_king)
tilted_towers.set_character(jonesy)
weeping_woods.set_character(midas)
loot_lake.set_character(brutus)
flush_factory.set_character(meowscles)
spawn_island.set_character(sky)
shifty_shafts.set_character(peely)

#Items
rocket_launcher = Item("Rocket Launcher")
rocket_launcher.set_description("A powerful weapon that deals massive damage.")
tilted_towers.set_item(rocket_launcher)

shadow_bomb = Item("Shadow Bomb")
shadow_bomb.set_description("Allows you to become invisible for a short time.")
pleasant_park.set_item(shadow_bomb)

medkit = Item("Medkit")
medkit.set_description("Restores full health.")
loot_lake.set_item(medkit)

shield_potion = Item("Shield Potion")
shield_potion.set_description("Grants additional shield protection.")
weeping_woods.set_item(shield_potion)

minigun = Item("Minigun")
minigun.set_description("A rapid-fire weapon that's effective in close combat.")
flush_factory.set_item(minigun)

boom_bow = Item("Boom Bow")
boom_bow.set_description("A bow that shoots explosive arrows.")
spawn_island.set_item(boom_bow)

slurp_juice = Item("Slurp Juice")
slurp_juice.set_description("A drink that gradually restores health and shield.")
shifty_shafts.set_item(slurp_juice)

bag = []
current_cave = pleasant_park #start at pleasant park
dead = False
health = 100 #health, updates when shield, medkit or slurp is used

while not dead:
    print("\n")
    current_cave.get_details()
    inhabitant = current_cave.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    item = current_cave.get_item()
    if item is not None:
        item.describe()
    command = input("What do you wish to do next: ")
    
    if command in ["north", "south", "east", "west"]:
        current_cave = current_cave.move(command)
    elif command == "talk":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.talk()
            talkinpt =  input("What do you wish to say next, Option 1, 2 or 3? ")
            if talkinpt == "1":
                print("You say: Have a good day mate!")
            elif talkinpt == "2":
                print("You say: Stay safe out there!")
            elif talkinpt == "3":
                print("You say: Nice to meet you!")
        else: print("There is nobody friendly to talk to.")
    elif command == "fight":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("What will you fight with?")
            fight_with = input()
            if fight_with in bag:
                if inhabitant.fight(fight_with):
                    print("Nice work! You won the fight and live to fight another day!")
                    current_cave.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have survived another adventure!")
                        dead = True #to restart
                else:
                    print("You lost the fight. The game ends here.")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")
    elif command == "pat":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("You should'nt do that...")
            else:
                inhabitant.pat()
        else:
            print("There is nobody here to pat right now. >:()")
    elif command == "take":
        if item is not None:
            print("You placed the " + item.get_name() + " in your bag")
            bag.append(item.get_name())
            current_cave.set_item(None)
    elif command == "bribe":
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            print("You bribe " + inhabitant.name + ". They let you pass safely.")
            current_cave.set_character(None)
        else:
            print("There is no one here to bribe")
    elif command == "hug":
        if inhabitant is not None and isinstance(inhabitant, Friend):
            inhabitant.hug()
        else:
            print("There is no one here to hug")
    elif command == "gift" and isinstance(inhabitant, Enemy): #if gift given to enemy, they die
        if inhabitant is not None:
            yesorno = input("Are you sure you wish to gift an enemy? ")
            if yesorno.lower() == "yes":
                gift = input("What do you wish to gift? ")
                if gift in bag:
                    inhabitant.receive_gift(gift)
                    current_cave.set_character(None)
            if yesorno.lower() == "no":
                dead = True
                print("Your rudeness gets you killed.")   
    elif command == "gift" and isinstance(inhabitant, Friend):
        gift = input("What do you wish to gift? ")
        if gift in bag:
            inhabitant.receive_gift(gift)
        else: print("You don't have a" + gift + "to give")
    


    
    if command == "use Shield":
        if shield_potion.get_name():
            health += 50
            print("\nYou used a Shield Potion. Your health is now: " , health)
        else:
            print("You don't have a Shield Potion in your bag.")
    if command == "use Medkit":
        if medkit.get_name() in bag:
            health += 100
            print("\nYou used a Medkit. Your health is now:" , health)
        else:
            print("You don't have a Medkit in your bag.")
    if command == "use Slurp Juice":
        if slurp_juice.get_name() in bag:
            health += 25
            print("\nYou used a Slurp Juice. Your health is now: " , health)
        else:
            print("You don't have a Slurp Juice in your bag.")

def find_easter_egg(): #50/50 chance of getting either items after each command input
    easter_eggs = ["Golden Scar", "Chug Jug", "Mythic Drum Gun"] 
    if random.choice([True, False]):
        egg = random.choice(easter_eggs)
        print(f"You found an Easter egg: {egg}!")
        bag.append(egg)

    find_easter_egg()



