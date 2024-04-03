from flask import Flask
import random

app = Flask(__name__)

# Generate a random number between 0 and 9
SECRET_NUMBER = random.randint(0, 9)


@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200>'


@app.route('/<int:guess>')
def guess_number(guess):
    if guess < SECRET_NUMBER:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=200>'
    elif guess > SECRET_NUMBER:
        return '<h1 style="color: blue;">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=200>'
    else:
        return '<h1 style="color: green;">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=200>'


if __name__ == "__main__":
    app.run(debug=True)
