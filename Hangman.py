import getpass
Word = ""
Guesses = -1
GuessedLetters = ""
def Intro():
	global Word, Guesses
	print("Welcome to Hangman!")
	Input = getpass.getpass(prompt="Player 1, input your word: ")
	Word = Input
	while True:
		chances = input("How many incorrect chances should Player 2 have? ")
		if type(chances) == int:
			chances = int(chances)
			break
	Guesses = chances
	print("\nPlayer 2, your turn!\n\nThe word is 5 letters long.")

def WordUpdate():
	
