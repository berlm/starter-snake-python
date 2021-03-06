import os
import random

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    # This function is called when you register your Battlesnake on play.battlesnake.com
    # It controls your Battlesnake appearance and author permissions.
    # TIP: If you open your Battlesnake URL in browser you should see this data
    return {
        "apiversion": "1",
        "author": "berlm",
        "color": "#ff9900",
        "head": "smile",
        "tail": "round-bum",
    }


@app.route('/start', methods=['POST'])
def start():
    # This function is called everytime your snake is entered into a game.
    # cherrypy.request.json contains information about the game that's about to be played.
    # TODO: Use this function to decide how your snake is going to look on the board.
    # data = cherrypy.request.json

    print("START")
    return "ok"


@app.route('/move', methods=['POST'])
def move():
    # This function is called on every turn of a game. It's how your snake decides where to move.
    # Valid moves are "up", "down", "left", or "right".
    # TODO: Use the information in cherrypy.request.json to decide your next move.
    data = request.json

    # Choose a random direction to move in
    possible_moves = ["up", "down", "left", "right"]
    selected = random.choice(possible_moves)

    print(f"MOVE: {selected}")
    return {"move": selected}


@app.route('/end', methods=['POST'])
def end():
    # This function is called when a game your snake was in ends.
    # It's purely for informational purposes, you don't have to make any decisions here.
    data = request.json

    print("END")
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
