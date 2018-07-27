word = input("falafel")

# Converts the word to lowercase
word = word.lower()

# Checks if only letters are present (isalpha means it has no numbers)
if(word.isalpha() == False):
	print("That's not a word!")

# Some useful variables
guesses = []
maxfails = 7

# make  a list of blank spaces
spaces = []
for letter in word:
	spaces.append("_")
len(word)
# check if one letter, make it lowercase
while maxfails > 0:
	if "_" not in spaces:
		print("You win!")
		break

	guess = input("Guess a letter")

# tell how many fails left
	guess = guess.lower()
# check if letter has been guessed already
	if guess in guesses:
		print("You already guessed that")
	if not (guess.isalpha() and len(guess) == 1):
		print("That's not a letter!")
	else:
		if guess in guesses:
			print("You already guessed that. Try Again")
		else:
			guesses.append(guess)
		if guess in word:
			for letter in range(len(word)):
				if guess == word[letter]:
					spaces[letter] = guess
			print("Correct!")
		else:
			maxfails -= 1
			print("Wrong!")
			print("You have "+str(maxfails) + "chances left")
	print(spaces)



# if the letter is in word, add it to the blank spaces

# if not in the word, record it as a "failure"

# add letter to list of guesses

# if spaces are full, win

# if max fails are reached, lose

# check every letter in word to see if = guessed letter
