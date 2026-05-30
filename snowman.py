import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___
     /___\\
     (o o)
     ( : )
     ( : )
     """,
     # Stage 1: Bottom part starts melting
     """
      ___
     /___\\
     (o o)
     ( : )
     """,
     # Stage 2: Only the head remains
     """
      ___
     /___\\
     (o o)
     """,
     # Stage 3: Snowman completely melted
     """
      ___
     /___\\
     """
 ]


def get_random_word():
	"""Selects a random word from the list."""
	return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word):
	"""Displays the game state."""
	print(STAGES[mistakes])
	print("Word: ", end=" ")
	for letter in secret_word:
		print("_", end=" ")
	print("\n\n")


def play_game():
	secret_word = get_random_word()
	mistakes = 0
	print("Welcome to Snowman Meltdown!")
	print("Secret word selected: " + secret_word)  # for testing, later remove this line
	
	# TODO: Build your game loop here.
	while mistakes < 4:
		display_game_state(mistakes=mistakes, secret_word=secret_word)
		# For now, simply prompt the user once:
		guess = input("Guess a letter: ").lower()
		print("You guessed:", guess)
		mistakes += 1   # for testing, later the game logic has to evalaute wether or not a mistake happened


if __name__ == "__main__":
	play_game()