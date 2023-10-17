# The Dragon Adventure Game
Adventure Game is a text-based decision game where you, the player, are presented with a series of choices.
Your decisions influence the outcome of the story, leading to various endings.
![Screenshot 2023-10-16 at 23 52 11](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/7761de0e-9376-494a-b2b3-1c054d4d1d76)

 [Link to the Live wetbsite](https://adventuregame-700241cd99d6.herokuapp.com/) 
 
## Table of Contents

#### • Game Overview

### • How to Play

### • Decision Points

### • Getting Started

### • Flowchart

### • Testing

### • Fixed bugs

### • Credits

### • License

## Game Overview
After introducing yourself, you find yourself in front of three mysterious doors. 
Each door leads to a different adventure:

• Door 1: Enter the Dragon's Lair
• Door 2: Discover a Treasure Room
• Door 3: Step into a Magic Room with Glowing Potions

Your decisions will determine your fate in this game!

## Game Mechanics
Begin by entering your name.
Choose one of the three doors to enter a room.
Make decisions based on the room's narrative and potential items in your inventory.
Potions from the Magic Room can greatly affect the outcome in the Dragon Room.
The game continues until you decide to stop or meet an unfortunate end.

Remember, each choice you make can lead to a different outcome. 
Play multiple times to explore all possible endings!

## Decision Points

### Dragon's Lair: 
Decide to steal the dragon's gold, sneak around, or confront the dragon.
### Treasure Room: 
Choose to open a chest or leave without seeing what's inside.
### Magic Room: 
Drink a potion to get an ability or leave without drinking anything.
Decisions in one room might influence the outcome in another!

##### Enhanced User Input: 
I used the helper function get_user_input() to take care of trimming and lowercasing the input.
##### Changed the Potion Logic: 
I've made the logic for the potions more straightforward. Now there is one potion for invisibility, 
one for strength, and one that takes the player back to the start. 
This will makes the game's progression clearer.
##### Play Again Logic: 
The logic for playing the game again or quitting has been simplified, 
which makes it more efficient.

# Getting Started
Copy the game code into a Python file
Run the game in your terminal or command prompt:
Follow the on-screen prompts and make your choices.

# Flowchart

### Start:

• A "Start" oval at the top.
### Enter Name:
• Below the "Start", a rectangle box labeled "Enter Name" connected with an arrow from the "Start" oval.

### Welcome Screen:
• An arrow from the "Enter Name" box leading to a parallelogram (used to depict inputs/outputs) with "Welcome to the Adventure Game!" and the three door choices.

### Decision Box for Door Choice:
• A diamond (used to represent decisions) with the question, "Which door?"
Three arrows emerging from the diamond, each labeled "1", "2", and "3" respectively.

### Dragon Room:
• For the "1" arrow, lead to a rectangle labeled "Dragon Room".
• Within the "Dragon Room" section, another decision diamond asking what the player wants to do with arrows for the three options and their respective outcomes.

### Treasure Room:
• For the "2" arrow, lead to a rectangle labeled "Treasure Room".
• Another decision diamond for the chest choice, with arrows for the options and their outcomes.

### Magic Room:
• For the "3" arrow, lead to a rectangle labeled "Magic Room".
• Another decision diamond for the potion choice, with arrows for the options and their outcomes. If the green potion is chosen, loop back to the "Welcome Screen" parallelogram.

### Play Again?:
• From all outcomes, arrows should lead to a decision diamond labeled "Play Again?".
• Two arrows emerge from this diamond, one for "yes" and one for "no". The "yes" arrow loops back to the "Welcome Screen" parallelogram, while the "no" arrow leads to the end.

### End:
• An "End" oval at the bottom.

Here is a final flowchart design.
![Screenshot 2023-10-17 at 20 12 54](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/f4c8310e-8431-434e-87ff-f80629c2bbdd)

# Testing

## Requirements:
Python3 run,py
[Enter your name]
"Greetings, [Your Name]!"

### Test Door Choices
Purpose: Ensure that all door choices lead to the correct rooms.
the "invisibility potion" or "strength potion" in the inventory affects the outcomes.
Run the game.
Purpose: Ensure that the game correctly captures and displays the user's name.
![Screenshot 2023-10-14 at 21 36 57](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/77056c36-3373-4414-98f4-ac6891a50660)

### Choose a door (1, 2, or 3).
Verify that the game takes you to the correct room (Dragon, Treasure, or Magic room).
### Test Inventory System
Purpose: Ensure items are correctly added to or removed from the inventory.

### Navigate to the Treasure Room.
Choose to open the chest.
Verify that the gem is added to the inventory.
Restart the game and verify that the inventory is cleared.
![Screenshot 2023-10-14 at 23 07 57](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/1a0834f8-aea8-4354-9334-b46b3bad01fa)

### Test Potion Choices in Magic Room
In the Magic room, here is the test of the two choices: drink a potion and leave the room.
When choosing to drink a potion, test all three options: blue, red, and green.
Ensure that the selected potion (invisibility or strength) affects the game's outcome.
Confirm that choosing "green" returns you to the start of the game.

![Screenshot 2023-10-14 at 23 27 41](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/e8c95840-d952-4e8b-bf88-39b6a1e05628)
![Screenshot 2023-10-14 at 23 28 31](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/9810c12f-ccc8-4a88-b218-f72110b34deb)

### Test Dragon Room Scenarios
In the Dragon room, test all three choices: steal gold, sneak around, confront the dragon.
Check that the dragon's reactions are appropriate based on your choices.
Verify that having the "invisibility potion" or "strength potion" in the inventory affects the outcomes.

###  Test Play Again Feature
 Ensure the game restarts correctly and clears the inventory.
 ![Screenshot 2023-10-14 at 23 54 24](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/6cc49c2a-97a0-4108-929a-4c40a2905800)
![Screenshot 2023-10-14 at 23 58 39](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/ca922b72-ff22-4f6b-899c-2edc800e2620)

### test invalid input
At any choice prompt, enter an invalid input (e.g., a letter or an out-of-range number).
Verify that the game informs you of the invalid choice.
![Screenshot 2023-10-15 at 00 11 46](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/0dc8f8fc-edbe-48f1-9b5d-530a50747901)

### Play Again
Test the "play again" feature at the end of each scenario.
Confirm that choosing "yes" resets the game, clearing the inventory.
Verify that choosing "no" exits the game with a farewell message.

# fixed bugs
Had a problem when runing the code in the terminal it showed error.
because else was on a wrong line.
![Screenshot 2023-10-15 at 08 16 11](https://github.com/JoannaAdermark1/The_Dragon_Room/assets/137285482/65a18caf-ffd2-46f6-881b-4662799547db)

In the magic_room() function, there was a typo in the message for the red potion. The sentence 
"You gives a strength boost, which can be used to confront the dragon.!" changed it too
"You get a strength boost, which can be used to confront the dragon!".

# Deployment

#### Was deployed using Heroku with the following steps:

Login to Heroku Create an account if necessary.

Click New in the Heroku dashboard and select ”Create new app.”

Write a name for the app and choose your region and click ”Create App.”

Added two build pack scripts : 
Python and Nodejs in that order where python is on top of Nodejs

Connected Heroku with GitHub account and the repository that is been working on

At the bottom, choose to either automatic deploment or manual deploment,
if you set to automatic you every time you make changes with your code and commit, heroku updated the changes.


# Credits 
Basic structure and understanding about python adventures are taken from

LeMaster Tech
https://youtu.be/u8X6TiJA8as?si=yDFeCzAcpqjCBGgI

Shaun Halverson
and https://youtu.be/ORsJn-71__0?si=t5m-KueXCC8uNOoj

# Acknowledgements
My Mentor Jubril.

Tutor support and student care at Code Institute for their support.

# License
This game is open-source and free to use, modify, and distribute. Enjoy and have fun!
