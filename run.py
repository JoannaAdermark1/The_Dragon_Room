name = input('Enter your name! ')
print(f'Greetings {name}!')

### print a welcome message
print("Welcome to the Dragon Room! ")
print("You find yourself at the entrance of a dark cavern ")
print("The legends spoke of this place: The Dragon Room.")
print("Do you wish to enter the Gold path, Darkness path, or cries path? ")
   
### prompt user for a choice

 Choice = input("Which path do you choose? (Gold/Darkness): ")

    if (roomchoice == "Gold path"):
        print("you enter the Gold path.")
        print("You find yourself collecting gold coins but then fall into a pit.")
        print("You're given a choice to buy a rope with some of your gold to climb out")
        print("Do you give up some gold for a rope (Yes/No):")

        if(ropechoice == "yes"):
            print("you climb out and leave with your other gold safely")
        elif(ropechoice == "no"):
            print("Your weight from the gold pulls you further down, and you're trapped.")
            print("dragon find you and eat you")
        else:
        end_game("You remain outside, forever wondering what adventures lay within the Dragon .")


    if (roomchoice == "darkness path"):
        print("you eneter darkness path.")
        print(" Here, you're given the choice between a sword bathed in light and a cloak of shadows")
        print("Depending on your choice,")
        print("you'll either face goblins (with the sword) or stealthily navigate the path (with the cloak)")
        print("Which do you choose? (Sword/Cloak): ")

       if (choice == "Sword"):
           print("Wielding the sword, you encounter goblins. They're blinded by its glow, giving you the advantage.")
           print("After defeating them, you find a door with a dragon emblem.")
       elif (choice == "Cloak"):
        print("Wrapped in shadows, you bypass creatures unseen. At the end of the path, there's a door with the dragon emblem.")
       else:
        end_game("Lost in uncertainty, a creature of the dark finds you.")

     if (roomchoice == "cries path"):
        print("Following the distant cries, you discover a prison cell. Inside is an elf, bound and trapped.")
    choice = input("Do you release the elf? (Release/Leave): ")
    if choice == "Release":
        print("Grateful, the elf guides you through hidden passageways, leading you directly to a door with a dragon emblem.")
        dragon_door()
    else:
        end_game("The cries of the elf haunt you as you wander aimlessly, eventually finding yourself back at the cavern entrance.")







