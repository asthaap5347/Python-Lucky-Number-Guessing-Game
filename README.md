# Lucky Number Guessing Game

A simple Python guessing game where the computer generates a random lucky number between 1 and 50, and the user tries to guess it.

## How It Works

1. The computer randomly generates a number between 1 and 50.
2. The user enters a number as their guess.
3. The program checks the guess against the lucky number.
4. If the guess is greater than the lucky number, it displays `Too high`.
5. If the guess is smaller than the lucky number, it displays `Too low`.
6. The game continues until the user guesses the correct number.
7. When the correct number is guessed, the game displays `You Won. Game Over!`

## Requirements

- Python 3.x

## How to Run

Run the following command in the terminal:

python lucky_number_game.py

## Example

Guess the lucky number: 25
Too low

Guess the lucky number: 40
Too high

Guess the lucky number: 32
You Won. Game Over!

Thank you for playing.

## Concepts Used

* Python functions
* `while` loops
* `if`, `elif`, and `else`
* User input
* Random number generation using the `random` module
* `break` statement
