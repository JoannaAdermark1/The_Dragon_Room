# Adventure Game
Adventure Game is a text-based decision game where you, the player, are presented with a series of choices.
Your decisions influence the outcome of the story, leading to various endings.

## Table of Contents
. Game Overview
. How to Play
. Decision Points
. Getting Started
. License

## Game Overview
After introducing yourself, you find yourself in front of three mysterious doors. 
Each door leads to a different adventure:

. Door 1: Enter the Dragon's Lair
. Door 2: Discover a Treasure Room
. Door 3: Step into a Magic Room with Glowing Potions

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

## Credits 
Basic structure and understanding about python adventures are taken from
LeMaster Tech
https://youtu.be/u8X6TiJA8as?si=yDFeCzAcpqjCBGgI

Shaun Halverson
and https://youtu.be/ORsJn-71__0?si=t5m-KueXCC8uNOoj

## License
This game is open-source and free to use, modify, and distribute. Enjoy and have fun!






![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome JoannaAdermark1 Adermark,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!
