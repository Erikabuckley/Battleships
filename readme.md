
## README
# Battleships Game

### Project Description
This Battleships game is like the classic two-player game where players attempt to sink their opponent's ships. It is built using python and designed to run using the command line and on a web browser using flask.

## Features List
These features have been implemented and are fully functional:
1. **Single player game**:
   - Ships are placed on a board.
   - User guessses where ships are
2. **Play against the computer**:
   - 2 boards are created, users board using a json file and the computers is random
   - Each player takes turns guessing
   - A new board is displayed and hit or miss is output
3. **Game with a GUI**:
   - Using flask a GUI has been implemented
   - This allows the user to see thier board and the computers board to guess
   - Game play alternates between user and computer until ships are sunk

### Installation
1. Clone this repository or download the source code zip.
   ```bash
   git clone [repository-link]
Battleships
The battleships game consists of two boards: one for the computer and one for the player. The player and computer take turns guessing coordinates to hit and sink all enemy boats. The game offers three board setup methods, and the web version provides a visual representation of the gameplay to enhance the user experience.


Features:
- Command-Line Version: Play Battleships via text-based input.
- Multiplayer Version: Play against the computer using the command line.
- Web Version: The battleships game with a graphical web interface.

Board Setup:
- Simple random placement.
- Custom placement options.

Gameplay Mechanics:
- Input coordinates to guess where enemy boats are placed.
- Visual and/or textual feedback on hits and misses.
- The game ends when one side loses all boats.

Prerequisites
- Python 3.x
- Flask
- Web browser


Installation
Downlaod zip file
Navigate to the project folder: cd battleships
Open a web browser and navigate to http://localhost:5000.


License
