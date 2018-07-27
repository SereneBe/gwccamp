# --- Define your functions below! ---
def intro():
    print("Hi, I'm Chatbot!")

def process_input(answer):
    if answer == "hi" or "hello" or "hey":
        print("Hello! Let's play rock, paper, scissors!")
    else:
        answer = input("Rock, Paper, or Scissors? ")

# make it say hi + name
def process_input(name):
    print("Hi" + name)

def main():
    name = input("(What's your name?)")
    say_hello(name)
    print("Hi" + name)

maxfails = 2



# --- Put your main program below! ---
def main():
    intro()
    while True:
        answer = input("(What will you say?) ")
        process_input(answer)

import random
myList = ("rock", "paper", "scissors") 
    if answer == ("rock" or "paper" or "scissors")
    print random.choice(myList)

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
# Converts the word to lowercase
word = word.lower()
guess = guess.lower()
# tell how many guesses or maxfails left
    maxfails -= 1
    print("You lost!")
    print("You have "+str(maxfails) + "chances left")
