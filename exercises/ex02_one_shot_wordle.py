"""EX02-One-shot Wordle."""
__author__ = "730571410"

secret_word: str = "python"

guess: str = input("What is your 6-letter guess? ")

index: int = 0
index_yellow: int = 0
wrong_place: bool = False
result: str = ""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(secret_word):
    guess = input("That was not 6-letters! Try again: ")

while index < len(secret_word):
    if secret_word[index] == guess[index]:
        result += GREEN_BOX
    else:
        while wrong_place is False and index_yellow < len(secret_word):
            if guess[index] == secret_word[index_yellow]:
                result += YELLOW_BOX
                wrong_place = True
            else:
                index_yellow += 1
                if index_yellow == len(secret_word):
                    result += WHITE_BOX
        wrong_place = False
        index_yellow = 0   
    
    index += 1

print(result)

if secret_word == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")