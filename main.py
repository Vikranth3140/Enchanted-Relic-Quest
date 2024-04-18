import random

def introduction():
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

    while is_alive:
        print("\nYou are at a crossroads. What do you want to do?")
        print("1. Go left")
        print("2. Go right")
        print("3. Go straight ahead")
        print("4. Quit game")

        choice = input("Enter your choice: ")

        if choice == "1":
            random_event(player_health, creature_health)
        elif choice == "2":
            random_event(player_health, creature_health)
        elif choice == "3":
            print("You encounter the mythical creature!")
            battle_result = battle(player_health, creature_health)
            if battle_result == "win":
                print("Congratulations! You retrieved the artifact and saved the kingdom.")
            else:
                print("You were defeated. Game over.")
            is_alive = False
        elif choice == "4":
            print("Exiting game.")
            is_alive = False
        else:
            print("Invalid choice. Please try again.")

def random_event(player_health, creature_health):
    event = random.choice(["trap", "treasure", "creature", "nothing"])

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
        battle_result = battle(player_health, creature_health)
        if battle_result == "win":
            print("You defeated the creature and continue your journey.")
        else:
            print("You were defeated by the creature. Game over.")
            quit()
    else:
        print("You explore the area but find nothing of interest.")

def battle(player_health, creature_health):
    while player_health > 0 and creature_health > 0:
        player_attack = random.randint(10, 20)
        creature_attack = random.randint(5, 15)

        print("\nPlayer health:", player_health)
        print("Creature health:", creature_health)

        print("1. Attack")
        print("2. Use potion")
        print("3. Retreat")

        battle_choice = input("Enter your choice: ")

        if battle_choice == "1":
            print("You attack the creature and deal", player_attack, "damage.")
            creature_health -= player_attack

            print("The creature attacks you and deals", creature_attack, "damage.")
            player_health -= creature_attack
        elif battle_choice == "2":
            potion_health = random.randint(15, 25)
            print("You use a potion and gain", potion_health, "health.")
            player_health += potion_health
        elif battle_choice == "3":
            print("You retreat from the battle.")
            return "lose"

    if player_health <= 0:
        return "lose"
    else:
        return "win"

if __name__ == "__main__":
    start_game()