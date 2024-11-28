# Imports modules needed for the game
import random
import json


# Function that returns a 2d array that represents the board state
def initialise_board(size=10):
    grid = [[None for i in range(size)] for j in range(size)]
    return (grid)


# Function that reads a file and creates a dictionary with the ships and their sizes
def create_battleships(filename='battleships.txt'):
    my_file = open(filename)
    battleships = {}
    for line in my_file:
        line = line.strip('\n')
        line = line.split(':')
        battleships[line[0]] = int(line[1])
    return (battleships)


# Function that updates the board data structure to position the ships on the board and returns it
def place_battleships(board, ships, algorithm='simple', ships_file='placement.json'):
    width = len(board)
    # Checks if boats are being placed in each row
    if algorithm == 'simple':
        row = 0
        boat_count = len(ships)
        # Adds each boat to the grid
        for boat, size in ships.items():
            count = size
            for i in range(width):
                if count != 0:
                    board[row][i] = boat
                    count -= 1
                else:
                    board[row][i] = None
            boat_count -= 1
            # Moves onto the next row
            row += 1
    # Checks if boat placement is random
    elif algorithm == 'random':
        # Goes through each ship
        for ship, size in ships.items():
            placed = False
            while not placed:
                # Picks random location
                too_long = 0
                oreintation = random.randint(0, 1)
                x = random.randint(0, width-1)
                y = random.randint(0, width-1)
                # If horisontal
                if oreintation == 0:
                    # Checks if it will fit in the board
                    if x < (width - size):
                        count = size
                        # Checks if placing will delete part of another boat
                        potential = board[y]
                        potential = potential[x:(x + size) - 1]
                        for element in potential:
                            if element != None:
                                too_long += 1
                        # Places element in the board
                        if too_long == 0:
                            for i in range(width):
                                pos = x + i
                                if count != 0:
                                    board[y][pos] = ship
                                    count -= 1
                            placed = True
                # If vertical
                elif oreintation == 1:
                    # Checks it will fit
                    if y < (width - size):
                        count = size
                        potential = []
                        for i in range(y, (y + size) - 1):
                            potential.append(board[i][x])
                            for element in potential:
                                if element != None:
                                    too_long += 1
                        if too_long == 0:
                            for i in range(width):
                                pos = y + i
                                if count != 0:
                                    board[pos][x] = ship
                                    count -= 1
                            placed = True
    # Checks if boats are being placed using a json file
    elif algorithm == 'custom':
        # Reads the data form the json file
        if ships_file == 'placement.json':
            with open(ships_file, 'r') as file:
                placement = json.load(file)
        else:
            placement = ships_file
        for ship, data in placement.items():
            oreintation = data[2]
            x = int(data[0])
            y = int(data[1])
            size = ships[ship]
            # If horisontal
            if oreintation == 'h':
                count = size
                # Places element in the board
                for i in range(width):
                    pos = x + i
                    if count != 0:
                        board[y][pos] = ship
                        count -= 1
            # If vertical
            elif oreintation == 'v':
                count = size
                # Places boat
                for i in range(width):
                    pos = y + i
                    if count != 0:
                        board[pos][x] = ship
                        count -= 1
    # Returns updated board
    return (board)
