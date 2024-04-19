import random
import os

def introduction():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to the Quest for the Enchanted Relic!")
    print("You are on a quest to retrieve a magical artifact from a mythical creature's lair.")
    print("This artifact is crucial for restoring peace to the kingdom.")
    print("Your journey begins at the entrance to the creature's lair.")
    print("Let's see if you have what it takes to succeed!\n")

def start_game():
    introduction()
    player_health = 100
    creature_health = 100
    is_alive = True
    inventory = {}

    while is_alive:
        print("\nYou are at a crossroads. What do you want to do?")
        print("1. Go left")
        print("2. Go right")
        print("3. Go straight ahead")
        print("4. Check inventory")
        print("5. Quit game")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3"]:
            random_event(player_health, creature_health, inventory)
        elif choice == "4":
            display_inventory(inventory)
        elif choice == "5":
            print("Exiting game.")
            is_alive = False
        else:
            print("Invalid choice. Please try again.")

    print("\nGame over.")
    if player_health <= 0:
        print("You were defeated. Game over.")
        quit()
    else:
        print("You escaped with the artifact. Victory!")
        quit()

def random_event(player_health, creature_health, inventory):
    event = random.choice(["trap", "treasure", "creature"])

    if event == "trap":
        trap_damage = random.randint(10, 30)
        print("You encounter a trap! You lose", trap_damage, "health.")
        player_health -= trap_damage
    elif event == "treasure":
        treasure_health = random.randint(20, 40)
        print("You find a treasure chest! You gain", treasure_health, "health.")
        player_health += treasure_health
    elif event == "creature":
        print("You encounter a hostile creature!")
        battle_result = battle(player_health, creature_health, inventory)
        if battle_result == "win":
            print("You defeated the creature and continue your journey.")
        else:
            print("You were defeated by the creature. Game over.")
            quit()
    else:
        print("You explore the area but find nothing of interest.")

def battle(player_health, creature_health, inventory):
    while player_health > 0 and creature_health > 0:
        player_attack = random.randint(10, 20)
        creature_attack = random.randint(5, 15)

        print("\nPlayer health:", player_health)
        print("Creature health:", creature_health)

        print("1. Attack")
        print("2. Use item")
        print("3. Retreat")

        battle_choice = input("Enter your choice: ")

        if battle_choice == "1":
            print("You attack the creature and deal", player_attack, "damage.")
            creature_health -= player_attack

            print("The creature attacks you and deals", creature_attack, "damage.")
            player_health -= creature_attack
        elif battle_choice == "2":
            use_item_from_inventory(player_health, creature_health, inventory)
        elif battle_choice == "3":
            print("You retreat from the battle.")
            return "lose"

    if player_health <= 0:
        return "lose"
    else:
        return "win"

def use_item_from_inventory(player_health, creature_health, inventory):
    print("Items in inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
    item_to_use = input("Enter the item you want to use: ")
    if item_to_use in inventory and inventory[item_to_use] > 0:
        if item_to_use in ["Potion", "Sword", "Shield", "Scroll of Fireball"]:
            item_effect(player_health, creature_health, inventory, item_to_use)
        else:
            print("You cannot use this item in battle as you do not have in in your inventory.")
    else:
        print("Item not found in inventory or quantity insufficient.")

def item_effect(player_health, creature_health, inventory, item_to_use):
    if item_to_use == "Sword":
        player_health += 20
        remove_item_from_inventory(inventory, "Sword", 1)
        print("You found a powerful sword! Your attack damage is increased.")
    elif item_to_use == "Shield":
        player_health -= 10
        remove_item_from_inventory(inventory, "Shield", 1)
        print("You obtained a sturdy shield! You take reduced damage in battles.")
    elif item_to_use == "Scroll of Fireball":
        creature_health -= 50
        remove_item_from_inventory(inventory, "Scroll of Fireball", 1)
        print("You acquired a Scroll of Fireball! You can use it to deal massive damage in battles.")
    elif item_to_use == "Potion":
        potion_health = random.randint(15, 25)
        player_health += potion_health
        remove_item_from_inventory(inventory, "Potion", 1)
        print(f"You found a healing potion! You can use it to restore health during battles. You gain {potion_health} health.")

def add_item_to_inventory(inventory, item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def remove_item_from_inventory(inventory, item, quantity):
    if item in inventory and inventory[item] >= quantity:
        inventory[item] -= quantity
        if inventory[item] == 0:
            del inventory[item]
        print(f"{quantity} {item}(s) removed from inventory.")
    else:
        print("Item not found in inventory or quantity insufficient.")

def display_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        print("Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")

if __name__ == "__main__":
    start_game()