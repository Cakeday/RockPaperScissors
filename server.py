from flask import Flask, render_template, request
import random

app = Flask(__name__)

logic = {"Rock": {"Rock": "tie", "Paper": "lose", "Scissors": "win"},
         "Paper": {"Rock": "win", "Paper": "tie", "Scissors": "lose"},
         "Scissors": {"Rock": "lose", "Paper": "win", "Scissors": "ties"}}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play', methods=['POST'])
def play():
    computer = str(assign(randInt(0, 2)))
    player = request.form['gesture']
    result = logic[player][computer]
    return render_template('result.html', result=result, computer=computer)


def assign(num):
    if (num == 0):
        num = "Rock"
    elif (num == 1):
        num = "Paper"
    else:
        num = "Scissors"
    return num


def randInt(min=0, max=100):
    if(min < 0 or min > max):
        min = 0
    if(max == 0):
        max = 1
    num = random.random()
    num = round(num*(max-min)) + min
    return num


if __name__ == "__main__":
    app.run(debug=True)
