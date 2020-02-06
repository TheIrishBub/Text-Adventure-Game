from textwrap import dedent
import random

print(dedent("""Please help us, brave warrior!
You must help us, because the dragon is terrorizing our village!
In order to appease the dragon, we have to sacrifice one of our village
maidens, unless someone brave goes to slay the dragon!
Please, you must help us! Go forth, and slay the beast!"""))

print(dedent("""\nYou find the cave near the village and enter.
After walking along, you find a treasure chest guarded by a bat.
You engage the bat!"""))

# Bat fight

bat_hp = 10
bat_attack = 5
bat_defense = 0
player_hp = 50
player_attack = 5
player_defense = 5

while player_hp > 0 and bat_hp > 0:

    print(dedent("""\nWhat will you do?
    1. Attack
    2. Defend
    3. Heal"""))

    choice = input("> ")

    if choice == "1":
        damage = player_attack - bat_defense + random.randint(0, 5)
        bat_hp = bat_hp - damage
        if bat_hp < 0:
            print(dedent(f"""You dealt {damage} damage and defeated the bat!
            You found a Short Sword, and your attack power goes up by 10!"""))
        else:
            print(f"You dealt {damage} damage! The bat has {bat_hp} health left.")
            damage = bat_attack - player_defense + random.randint(0, 5)
            if bat_hp > 0:
                player_hp = player_hp - damage
                print(f"The bat hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '2':
        damage = bat_attack - player_defense + random.randint(0, 5) - 5
        if damage < 0:
            damage = 0
        player_hp = player_hp - damage
        print(f"The bat hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '3':
        healing = 20 + random.randint(0,5)
        player_hp = player_hp + healing
        if player_hp > 50:
            player_hp = 50
        print(f"\nYou restored {healing} health. You have {player_hp} health.")

    else:
        print("Try again.")

print(dedent("""\nYou continue forward, and as you go, you start to feel a chill
in the air. You are wondering why you are feeling so cold when suddenly,
a menacing ghost comes out of nowhere and attacks you!"""))

# Ghost fight

ghost_hp = 40
ghost_attack = 10
ghost_defense = 0
player_hp = 50
player_attack = 15
player_defense = 5

while player_hp > 0 and ghost_hp > 0:

    print(dedent("""\nWhat will you do?
    1. Attack
    2. Defend
    3. Heal"""))

    choice = input("> ")

    if choice == "1":
        damage = player_attack - ghost_defense + random.randint(0, 5)
        ghost_hp = ghost_hp - damage
        if ghost_hp < 0:
            print(dedent(f"""You dealt {damage} damage and defeated the ghost!
            You found a Leather Armor, and your defense goes up by 5!"""))
        else:
            print(f"You dealt {damage} damage! The ghost has {ghost_hp} health left.")
            damage = ghost_attack - player_defense + random.randint(0, 5)
            if ghost_hp > 0:
                player_hp = player_hp - damage
                print(f"The ghost hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '2':
        damage = ghost_attack - player_defense + random.randint(0, 5) - 5
        if damage < 0:
            damage = 0
        player_hp = player_hp - damage
        print(f"The ghost hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '3':
        healing = 20 + random.randint(0,5)
        player_hp = player_hp + healing
        if player_hp > 50:
            player_hp = 50
        print(f"\nYou restored {healing} health. You have {player_hp} health.")

    else:
        print("Try again.")

print(dedent("""\nAfter defeating the ghost, you move on to an area of the cave that
resembles a graveyard. As you explore this new area, you examine all the
graves. When looking at the back row, you hear a shuffling sound coming
from the side. You turn to look, and see a skeleton rising from its grave.
The skeleton, wanting to take you with him, attacks you!"""))

# Skeleton fight

skeleton_hp = 50
skeleton_attack = 15
skeleton_defense = 5
player_hp = 50
player_attack = 15
player_defense = 5

while player_hp > 0 and skeleton_hp > 0:

    print(dedent("""\nWhat will you do?
    1. Attack
    2. Defend
    3. Heal"""))

    choice = input("> ")

    if choice == "1":
        damage = player_attack - skeleton_defense + random.randint(0, 5)
        skeleton_hp = skeleton_hp - damage
        if skeleton_hp < 0:
            print(dedent(f"""You dealt {damage} damage and defeated the skeleton!
            You found a Long Sword, and your attack power goes up by 10!"""))
        else:
            print(f"You dealt {damage} damage! The skeleton has {skeleton_hp} health left.")
            damage = skeleton_attack - player_defense + random.randint(0, 5)
            if skeleton_hp > 0:
                player_hp = player_hp - damage
                print(f"The skeleton hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '2':
        damage = skeleton_attack - player_defense + random.randint(0, 5) - 5
        if damage < 0:
            damage = 0
        player_hp = player_hp - damage
        print(f"The skeleton hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '3':
        healing = 20 + random.randint(0,5)
        player_hp = player_hp + healing
        if player_hp > 50:
            player_hp = 50
        print(f"\nYou restored {healing} health. You have {player_hp} health.")

    else:
        print("Try again.")

print(dedent("""\nAfter shaking off the skeleton, you decide to leave the
graveyard area of this cave. You take a path leading away from the graveyard,
when a goblin jumps out and ambushes you!"""))

# Goblin fight

goblin_hp = 100
goblin_attack = 10
goblin_defense = 0
player_hp = 50
player_attack = 25
player_defense = 5

while player_hp > 0 and goblin_hp > 0:

    print(dedent("""\nWhat will you do?
    1. Attack
    2. Defend
    3. Heal"""))

    choice = input("> ")

    if choice == "1":
        damage = player_attack - goblin_defense + random.randint(0, 5)
        goblin_hp = goblin_hp - damage
        if goblin_hp < 0:
            print(dedent(f"""You dealt {damage} damage and defeated the goblin!
            You found an Iron Armor, and your defense goes up by 10!"""))
        else:
            print(f"You dealt {damage} damage! The goblin has {goblin_hp} health left.")
            damage = goblin_attack - player_defense + random.randint(0, 5)
            if goblin_hp > 0:
                player_hp = player_hp - damage
                print(f"The goblin hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '2':
        damage = goblin_attack - player_defense + random.randint(0, 5) - 5
        if damage < 0:
            damage = 0
        player_hp = player_hp - damage
        print(f"The goblin hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '3':
        healing = 20 + random.randint(0,5)
        player_hp = player_hp + healing
        if player_hp > 50:
            player_hp = 50

    else:
        print("Try again.")

print(dedent("""\nWith the goblin slain, you continue on. As you find your way
to the back of the cave, you hear a roaring sound. You turn the corner to
discover the fearsome dragon that has been terrorizing the nearby village!
In order to restore peace, you start fighting the dragon."""))

# Dragon fight

dragon_hp = 150
dragon_attack = 20
dragon_defense = 5
player_hp = 50
player_attack = 25
player_defense = 15

while player_hp > 0 and dragon_hp > 0:

    print(dedent("""\nWhat will you do?
    1. Attack
    2. Defend
    3. Heal"""))

    choice = input("> ")

    if choice == "1":
        damage = player_attack - dragon_defense + random.randint(0, 5)
        dragon_hp = dragon_hp - damage
        if dragon_hp < 0:
            print(dedent(f"""You dealt {damage} damage and defeated the dragon!"""))
        else:
            print(f"You dealt {damage} damage! The dragon has {dragon_hp} health left.")
            damage = dragon_attack - player_defense + random.randint(0, 5)
            if dragon_hp > 0:
                player_hp = player_hp - damage
                print(f"The dragon hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '2':
        damage = dragon_attack - player_defense + random.randint(0, 5) - 5
        if damage < 0:
            damage = 0
        player_hp = player_hp - damage
        print(f"The dragon hit you for {damage} damage! You have {player_hp} health left.")

    elif choice == '3':
        healing = 20 + random.randint(0,5)
        player_hp = player_hp + healing
        if player_hp > 50:
            player_hp = 50
        print(f"\nYou restored {healing} health. You have {player_hp} health.")

    else:
        print("Try again.")


if player_hp <= 0:
    print("You died!")
else:
    print(dedent("""With the dragon defeated, you have restored peace to the village!
In celebration, the village throws a parade in your honor.
Congratulations!"""))
