from ascii_art import STAGES
import random

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
	secret_word = get_random_word()
	mistakes = 0
	guessed_letters = []
	print("Welcome to Snowman Meltdown!")

	while mistakes < 4:
		display_game_state(mistakes=mistakes, secret_word=secret_word, guessed_letters=guessed_letters)
		guess = input("Guess a letter: ").lower()
		if guess in secret_word and guess not in guessed_letters and len(guess) == 1:
			for i in range(secret_word.count(guess)): # For the right amount of times the guessed character appears
				guessed_letters.append(guess)
			if len(guessed_letters) == len(secret_word):
				break
		else:
			mistakes += 1

	# The Game come to an end, now according to the state (win | loose) print the final message
	if mistakes < 4:
		print("Congratulations, you saved the snowman!")
	else:
		print("Game Over! The word was:", secret_word)