"""EX01-Chardle"""
__author__ = "730571410"


secret_word: str = input("Enter a 5-character word: ")
if len(secret_word) != 5:
    print("Error: Word must contain 5 characters")
    quit()

first_guess: str = input("Enter a single character: ")
if len(first_guess) != 1:
    print("Error: Character must be a single character.")
    quit()

amount: int = 0
print("Searching for " + first_guess + " in " + secret_word)

if first_guess == secret_word[0]:
    print(first_guess + " found at index 0")
    amount = amount+1

if first_guess == secret_word[1]:
    print(first_guess + " found at index 1")
    amount = amount + 1

if first_guess == secret_word[2]:
    print(first_guess + " found at index 2")
    amount = amount + 1

if first_guess == secret_word[3]:
    print(first_guess + " found at index 3")
    amount= amount + 1

if first_guess == secret_word[4]:
    print(first_guess + " found at index 4")
    amount = amount + 1

if amount == 0:
    print("No instances of " + first_guess + " found in " + secret_word)

if amount == 1:
    print(str(amount) + " instance of " + first_guess + " found in " + secret_word) 

if amount > 1:
    print(str(amount) + " instances of " + first_guess + " found in " + secret_word) 
