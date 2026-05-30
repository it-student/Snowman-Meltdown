"""
This module contains functions with the game-logics.
It imports the ascii-art for the different stages from ascii_art.py.
"""
import random
from ascii_art import STAGES

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the game state."""
    print(STAGES[mistakes])
    print("Word: ", end=" ")
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("\n\n")


def play_game():
    """Plays the game."""
    # Initial variable setup and welcoming message:
    secret_word = get_random_word()
    mistakes = 0
    guessed_letters = []
    print("Welcome to Snowman Meltdown!")

    # Main Game Loop:
    while mistakes < 4:
        display_game_state(mistakes=mistakes,
                           secret_word=secret_word,
                           guessed_letters=guessed_letters)
        guess = input("Guess a letter: ").lower()
        if guess in secret_word and guess not in guessed_letters and len(guess) == 1:
            for _ in range(secret_word.count(guess)):  # for right number of appearances
                guessed_letters.append(guess)
            if len(guessed_letters) == len(secret_word):
                break
        else:
            mistakes += 1

    # print the final message  (win | loose)
    if mistakes < 4:
        print("Congratulations, you saved the snowman!")
    else:
        print("Game Over! The word was:", secret_word)

    # Ask the user for another round
    game_restart = input("Do you want to play again? (y/n): ").lower()
    if game_restart == "y":
        play_game()
