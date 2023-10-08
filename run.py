inventory = []

def start_game():
    print("Welcome to the Adventure Game!")
    print("You find yourself in front of three doors. Which door do you go through? Door #1, Door #2, or Door #3?")
    choice = input("> ")

    if choice == "1":
        dragon_room()
    elif choice == "2":
        treasure_room()
    elif choice == "3":
        magic_room()
    else:
        print("Invalid choice. Game over!")
        play_again()

def dragon_room():
    print("\nYou have entered the Dragon's lair!")
    print("The dragon is sleeping. What do you want to do?")
    print("1. Steal some of its gold.")
    print("2. Try to sneak around it to the exit.")
    
    choice = input("> ")

    if choice == "1":
        print("\nThe dragon wakes up and burns you with its fire. Game over!")
        play_again()
    elif choice == "2":
        if "invisibility potion" in inventory:
            print("\nUsing the invisibility potion, you sneak past the dragon and escape. You win!")
            play_again()
        else:
            print("\nThe dragon wakes up and sees you. Game over!")
            play_again()
    else:
        print("Invalid choice. Game over!")
        play_again()

def treasure_room():
    print("\nYou've found the treasure room!")
    print("There's a chest in front of you. Do you want to open it?")
    print("1. Yes, I want to see what's inside.")
    print("2. No, it might be a trap.")
    
    choice = input("> ")

    if choice == "1":
        print("\nThe chest contains a priceless gem. You add it to your inventory.")
        inventory.append("gem")
        play_again()
    elif choice == "2":
        print("\nYou decide to leave the room without the treasure.")
        play_again()
    else:
        print("Invalid choice. Game over!")
        play_again()

def magic_room():
    print("\nYou've entered a room filled with glowing potions.")
    print("A sign reads: 'Choose wisely, one grants invisibility, others bring misfortune.'")
    print("Do you:")
    print("1. Drink a potion.")
    print("2. Leave the room without drinking anything.")

    choice = input("> ")

    if choice == "1":
        potion_choice = input("\nThere are three potions: red, blue, and green. Which one do you drink? > ")

        if potion_choice == "blue":
            print("\nYou feel light and transparent... You've gained the power of invisibility!")
            inventory.append("invisibility potion")
            play_again()
        else:
            print("\nYou feel dizzy and fall unconscious. Game over!")
            play_again()
    elif choice == "2":
        print("\nYou decide to leave the room without drinking anything.")
        play_again()
    else:
        print("Invalid choice. Game over!")
        play_again()

def play_again():
    print("\nDo you want to play again? (yes or no)")
    choice = input("> ").lower()
    if choice == "yes":
        inventory.clear()
        start_game()
    elif choice == "no":
        print("Thanks for playing!")
    else:
        print("Invalid choice. Exiting game.")
        exit()

start_game()