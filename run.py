name = input('Enter your name! ')
print(f'Greetings {name}!')

def main():
    print("You find yourself at the entrance of a dark cavern: the Dragon Room.")
    print("Do you wish to enter the Dragon Room?")
    choice = input("(Enter/Not Enter): ")

    if choice == "Enter":
        first_chamber( )
    else:
        end_game("You remain outside, forever wondering what adventures lay within the Dragon Room.")

def first_chamber():
    print("A flickering torch reveals three distinct paths: Gold, Darkness, Cries.")
    choice = input("Which path do you choose? (Gold/Darkness/Cries): ")

    if choice == "Gold":
        gold_path(  )
    elif choice == "Darkness":
        darkness_path( ) 
    elif choice == "Cries":
        cries_path( )

def gold_path():
    print("You follow the glittering path and fall into a pit.")
    choice = input("Do you give up some gold for a rope? (Yes/No): ")

    if choice == "Yes":
        dragon_door(.  )
    else:
        end_game("Your weight from the gold pulls you further down, and you're trapped.")

