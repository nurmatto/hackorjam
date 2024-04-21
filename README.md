HackorJam 2024.
We have been inspired by a passion for creativity and innovation in crafting this thrilling gaming experience.
The authors of this game are Anara Armankyzy, Ayala Nurakyn, Meirambek Zhumagaliyev, Yerassyl Sabitov, Torebek Nurmukhamed.

 Documentation for Pygame Project "Stay Alive"

 1. Overview
Game Description:
"Stay Alive" is an action-packed game set in a post-apocalyptic world where players navigate through challenging environments, combat various enemies, and complete levels to progress in the game. It features rich animations, strategic combat, and dynamic environments.

 2. Getting Started

Prerequisites:
- Python 3.8 or newer
- Pygame library version 2.0

Installation Steps:
1. Ensure Python is installed on your system. Python can be downloaded from [python.org](https://python.org).
2. Install Pygame via pip:
     pip install pygame
3. Download the game source code from the repository or via a zip file.

Running the Game:
To start the game, navigate to the game's directory in your terminal or command prompt and run:python main.py

 3. Game Mechanics

Controls:
- Move: Use the W, A, S, D keys to move the player character.
- Attack: Press the Space bar to execute attacks.
- Pause/Exit: Press the Esc key to pause the game or exit to the main menu.

Gameplay Elements:
- Player: Manages the player character's movements, animations, and interactions.
- Enemy: Controls enemy behaviors, tracking, and interactions with the player.
- Animations: Handles loading and updating frame-based animations for different characters.

 4. Code Structure

Classes and Modules:
- Player: Manages player properties such as position, movement, and actions.
- Enemy: Defines enemy characteristics and automates enemy actions.
- Game: Central class that initializes the game, manages game states, and processes main game loop.
- Animation: Utility class for managing sprite animations based on Pygame.

Important Methods:
- move(): Updates the player's or enemy's position based on input or AI.
- draw(): Renders game entities on the screen.
- update(): Central update method called within the game loop to refresh game state.

 5. Development and Contribution

Contributing to the Project:
- Fork the repository and clone it locally, or download the source directly.
- Create a new branch for your features or fixes.
- Submit pull requests with detailed descriptions of changes and improvements.

Issue Reporting and Support:
- Report bugs and issues through the project's issue tracker on GitHub.
- For support, contact the development team via the provided email or through GitHub.

 6. License
This game is released under the MIT License, which allows for personal and commercial use, modification, distribution, and private use.

 7.Conclusion
This documentation aims to provide all necessary information for players and contributors to easily set up, understand, and contribute to the game. For detailed information on updates and project status, check the project repository or the official game website.
