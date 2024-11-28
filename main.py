# Imports the funtions from the other moduels and Flask and its methods
from flask import Flask, render_template, request, jsonify
from components import initialise_board, create_battleships, place_battleships
from game_engine import attack
import random

# Instantiates an app
app = Flask(__name__)

# Creating the players boards and dictionarys globally for easy acesss
global game_board_1
game_board_1 = initialise_board()
global ships_dict_1
ships_dict_1 = create_battleships()
# Creating the computers boards and dictionarys globally for easy acesss
global game_board_2
game_board_2 = initialise_board()
ships_dict_2 = create_battleships()
game_board_2 = place_battleships(game_board_2, ships_dict_2, 'random')


# Board placement interface
@app.route("/placement", methods=['GET', 'POST'])
def placement_interface():
    if request.method == 'GET':
        global game_board_1
        global ships_dict_1
        # Returns the page for the user to place their ships
        return render_template('placement.html', board_size=len(game_board_1), ships=ships_dict_1)
    if request.method == 'POST':
        global ships_dict_2
        global game_board_2
        # Gets the location of the ships form the page
        ships_json = request.get_json()
        game_board_1 = place_battleships(
            game_board_1, ships_dict_1, 'custom', ships_json)
        # Gives the user a mesage to say ships have been placed
        return jsonify({'message': 'Received'}), 200


# Attack function
@app.route("/attack")
def process_attack():
    # Gets coordinates user has clicked
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    coordinates = (x, y)

    global game_board_1
    global ships_dict_1
    global game_board_2
    global ships_dict_2
    # Checks if the coordinates are a hit or not
    hit, game_board_2 = attack(coordinates, game_board_2, ships_dict_2)

    if hit:
        v = ships_dict_2.values()
        print(v)
        # Checks if the game is over as all ships are sunk
        count = 0
        for element in v:
            if element != 0:
                count += 1
        # Checks if the comupters coodinates are a hit
        x = random.randint(0, len(game_board_1)-1)
        y = random.randint(0, len(game_board_1)-1)
        hit_c, game_board_1 = attack((x, y), game_board_1, ships_dict_1)

        if count != 0:
            return jsonify({'hit': True, 'AI_Turn': (x, y)})

        return jsonify({'hit': True, 'AI_Turn': (x, y), 'finished': 'Game Over player wins'})

    else:
        x = random.randint(0, len(game_board_1)-1)
        y = random.randint(0, len(game_board_1)-1)
        hit_c, game_board_1 = attack((x, y), game_board_1, ships_dict_1)
        if hit_c:
            v = ships_dict_1.values()
            # Checks if the game is over as all ships are sunk
            count = 0
            for element in v:
                if element != 0:
                    count += 1
            if count == 0:
                return jsonify({'hit': False, 'AI_Turn': (x, y), 'finished': 'Game Over computer wins'})

        return jsonify({'hit': False, 'AI_Turn': (x, y)})


# Renders the main playing screen
@app.route("/", methods=['GET'])
def root():
    return render_template('main.html', player_board=game_board_1)


# Checks code is running in global namespace
if __name__ == '__main__':
    app.run(debug=True)
