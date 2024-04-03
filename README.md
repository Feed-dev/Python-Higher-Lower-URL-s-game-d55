# Higher-Lower Game

Welcome to the **Higher-Lower Game**, a web-based adventure where your intuition and luck are your best allies. Built with Flask, this simple yet captivating game challenges you to guess a randomly selected number between 0 and 9. Are you ready to test your guessing prowess?

## How to Play

The game is straightforward:
1. Visit the home page and you'll be greeted with an invitation to guess a number between 0 and 9.
2. Enter your guess in the URL, for example, `/3` if you guess the number 3.
3. You'll receive immediate feedback:
   - If your guess is **too low**, you'll be encouraged to aim higher.
   - If your guess is **too high**, you'll be advised to lower your sights.
   - Guess correctly, and victory is yours!

Each outcome is accompanied by a thematic GIF to enhance your experience.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3
- Flask

You can install Flask using pip:

```bash
pip install Flask
```

Clone the repository to your local machine:

```bash
git clone https://your-repository-url/higher-lower.git
```

Navigate into the project directory:

```bash
cd higher-lower
```

Start the Flask application:

```bash
python server.py
```

Open your web browser and go to http://127.0.0.1:5000 to start playing.

