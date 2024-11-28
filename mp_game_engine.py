# Imports functions from the other game modules
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack
import random


#  Generate coordinates for the computer attack
def generate_attack(size):
    x = random.randint(0, size-1)
    y = random.randint(0, size-1)
    return (x, y)


# Main game function
def ai_opponent_game_loop():
    # Displays welcome messsage onscreen
    print('Hello welcome to battleships')

    # Creates users board and adds it to the dictionary
    player_1 = input('Enter a username: \n')
    game_board_1 = initialise_board()
    ships_dict_1 = create_battleships()
    game_board_1 = place_battleships(game_board_1, ships_dict_1, 'custom')
    players[player_1] = [game_board_1, ships_dict_1]

    # Creates computers board and adds it to the dictionary
    game_board_2 = initialise_board()
    ships_dict_2 = create_battleships()
    game_board_2 = place_battleships(game_board_2, ships_dict_2, 'random')
    players['computer'] = [game_board_2, ships_dict_2]

    # Section of code that iterates while the game is running
    over = False
    while not over:
        size = len(players['computer'][0])
        # Get x cordinate from user
        x_valid = False
        while not x_valid:
            x = input('What x coordinate would you like?')
            # Checks if x cordinate is valid
            if x.isdigit():
                x = int(x)
                if x < size and x >= 0:
                    x_valid = True
        # Get y coordinate
        y_valid = False
        while not y_valid:
            y = input('What y coordinate would you like?')
            # Checks if y coordinate is valid
            if y.isdigit():
                y = int(y)
                if y < size and y >= 0:
                    y_valid = True
        coordinates = (x, y)

        # Processes the attack
        hit, players['computer'][0] = attack(
            coordinates, players['computer'][0], players['computer'][1])
        if hit:
            print('Hit!\n')
            v = players['computer'][1].values()
            # Checks if the game is over as all ships are sunk
            count = 0
            for element in v:
                if element != 0:
                    count += 1
            if count == 0:
                over = True
                print('Game over, you win')
        else:
            print('Miss\n')

        # Generates computer attack
        coordinates = generate_attack(len(players[player_1][1]))

        # Checks if guess was sucsesful
        hit, players[player_1][0] = attack(
            coordinates, players[player_1][0], players[player_1][1])
        if hit:
            print('Computer got a hit!\n')
            v = players[player_1][1].values()
            # Checks if the game is over as all ships are sunk
            count = 0
            for element in v:
                if element != 0:
                    count += 1
            if count == 0:
                over = True
                print('Game over, computer wins')
        else:
            print('Comupter got a miss\n')
        # Displays the board to the user
        print('This is your current board:\n')
        for element in players[player_1][0]:
            print(*element)
        print('\n')


# Checks game is running in global namespace
if __name__ == '__main__':
    players = {}
    ai_opponent_game_loop()