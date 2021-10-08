from flask import Flask
from flask import request

import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return f"Let's play Rock Paper Scissors! just add /play in the URL and use the query string hand. It accepts the following values: rock,paper,scissors"

def rps_logic(computer: str, user: str):
    if user == 'rock':
        if computer == 'paper':
            return "You lose"
        if computer == 'scissor':
            return "You won"
        if computer == 'rock':
            return "It's a tie"
    if user == 'paper':
        if computer == 'paper':
            return "It's a tie"
        if computer == 'scissor':
            return "You lose"
        if computer == 'rock':
            return 'You won'
    if user == 'scissor':
        if computer == 'paper':
            return "You won"
        if computer == 'scissor':
            return "It's a tie"
        if computer == 'rock':
            return 'You lose'

@app.route('/play', methods=['GET'])
def hand():
    h = request.args.get('hand')
    print(f'HAND: {h}')
    choices = ['rock', 'paper', 'scissor']
    computer = random.choice(choices)
    user = h.lower()

    if user not in choices:
        return "Hand invalid"

    result = rps_logic(computer, user)
    response = f"""
            Computer: {computer} <br>
            You: {user} <br>
            Result: {result}
        """
    return response

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')