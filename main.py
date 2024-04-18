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
        print("5. Use item from inventory")
        print("6. Quit game")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_event(player_health, creature_health, inventory)
        elif choice == "2":
            random_event(player_health, creature_health, inventory)
        elif choice == "3":
            random_event(player_health, creature_health, inventory)
        elif choice == "4":
            display_inventory(inventory)
        elif choice == "5":
            use_item_from_inventory(player_health, inventory)
        elif choice == "6":
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
    event = random.choice(["trap", "treasure", "creature", "new_inventory", "random_item", "nothing"])

    if event == "trap":
        trap_damage = random.randint(10, 30)
        print("You encounter a trap! You lose", trap_damage, "health.")
        player_health -= trap_damage
    elif event == "treasure":
        treasure_health = random.randint(20, 40)
        print("You find a treasure chest! You gain", treasure_health, "health.")
        player_health += treasure_health
        add_random_item_to_inventory(inventory)
    elif event == "creature":
        print("You encounter a hostile creature!")
        battle_result = battle(player_health, creature_health)
        if battle_result == "win":
            print("You defeated the creature and continue your journey.")
        else:
            print("You were defeated by the creature. Game over.")
            quit()
    elif event == "new_inventory":
        print("You discover a hidden cache with a new inventory!")
        new_inventory = generate_random_inventory()
        merge_inventories(inventory, new_inventory)
    elif event == "random_item":
        print("You stumble upon a mysterious item!")
        random_item_effect(player_health, inventory)
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
            use_item_from_inventory(player_health, inventory)
        elif battle_choice == "3":
            print("You retreat from the battle.")
            return "lose"

    if player_health <= 0:
        return "lose"
    else:
        return "win"

def generate_random_inventory():
    items = ["Sword", "Shield", "Scroll of Fireball", "Potion"]
    new_inventory = {}
    for item in items:
        quantity = random.randint(1, 3)
        new_inventory[item] = quantity
    return new_inventory

def merge_inventories(inventory, new_inventory):
    for item, quantity in new_inventory.items():
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

def random_item_effect(player_health, inventory):
    random_item = random.choice(["Sword", "Shield", "Scroll of Fireball", "Potion"])
    if random_item == "Sword":
        player_health += 20
        print("You found a powerful sword! Your attack damage is increased.")
    elif random_item == "Shield":
        player_health -= 10
        print("You obtained a sturdy shield! You take reduced damage in battles.")
    elif random_item == "Scroll of Fireball":
       enemy_health -= 50
       print("You acquired a Scroll of Fireball! You can use it to deal massive damage in battles.")
    elif random_item == "Potion":
        potion_health = random.randint(15, 25)
        print(f"You found a healing potion! You can use it to restore health during battles. You gain {potion_health} health.")
        player_health += potion_health
def use_item_from_inventory(player_health, inventory):
    print("Items in inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")
    
    item_to_use = input("Enter the item you want to use: ")
    if item_to_use in inventory and inventory[item_to_use] > 0:
        if item_to_use == "Potion":
            potion_health = random.randint(15, 25)
            print("You use a potion and gain", potion_health, "health.")
            player_health += potion_health
            remove_item_from_inventory(inventory, "Potion", 1)
        else:
            print("You cannot use this item in battle.")
    else:
        print("Item not found in inventory or quantity insufficient.")

def add_random_item_to_inventory(inventory):
    items = ["Sword", "Shield", "Scroll of Fireball", "Potion"]
    item = random.choice(items)
    add_item_to_inventory(inventory, item, 1)

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