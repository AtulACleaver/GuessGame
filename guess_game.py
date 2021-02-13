import random

arrOfWords = ["words", "guess", "actions"]
secret_word = random.choice(arrOfWords)
guess = ""
chances = 3

while guess != secret_word and chances != 0:
    guess = input("What's your guess: ")
    if guess != secret_word and chances != 0:
        chances -= 1
        if chances > 0:
            print("It's wrong...")
            print("Continue, you have only ", chances, " chances left.")
    if guess != secret_word and chances == 0:
        print("You lost dude! Run the program again and try again!!")
    elif guess == secret_word:
        print("You win!!")
