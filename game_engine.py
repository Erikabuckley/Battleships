# Imports the functions from components module
from components import initialise_board, create_battleships, place_battleships


# Function to check if ship has been hit and modifies board accordingly
def attack(coordinates, board, battleships):
    x = coordinates[0]
    y = coordinates[1]
    val = board[x][y]
    if val == None:
        # Returns False if location guessed is empty
        return (False, board)
    # Checks if the battleship has been sunk or not
    elif battleships[val] > 1:
        battleships[val] = battleships[val] - 1
        board[x][y] = None
        return (True, board)
    else:
        # If boat sunk the length of the ship in the dictionary is set to 0
        battleships[val] = 0
        board[x][y] = None
        return (True, board)


# Gets user input of coordinates
def cli_coordinates_input():
    x_valid = False
    while not x_valid:
        x = input('What x coordinate would you like? \n')
        # Checks that the x is a valid guess: an integer in the dimensions of the board
        if x.isdigit():
            x = int(x)
            x_valid = True

    y_valid = False
    while not y_valid:
        y = input('What y coordinate would you like? \n')
        # Checks that the y is a valid guess: an integer in the dimensions of the board
        if y.isdigit():
            y = int(y)
            y_valid = True
    # Returns a valid guess
    return (x, y)


# Main game loop start
def simple_game_loop():
    # Set up the game by creating board
    print('Hello welcome to battleships')
    game_board = initialise_board()
    ships_dict = create_battleships()
    game_board = place_battleships(game_board, ships_dict)
    over = False
    # Asks for input from user and checks if ship has been hit or not
    while not over:
        coordinates = cli_coordinates_input()
        hit, game_board = attack(coordinates, game_board, ships_dict)
        if hit:
            print('Hit!')
            v = ships_dict.values()
            # Checks if the game is over as all ships are sunk
            count = 0
            for element in v:
                if element != 0:
                    count += 1
            if count == 0:
                over = True
        else:
            print('Miss')
    print('Game over')


# Runs the main game function
if __name__ == "__main__":
    simple_game_loop()
