"""EX03-Wordle."""
__author__ = "730571410"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(secret_word: str, guess: str) -> bool:
    """Searches for guess within secret_word"""
    assert len(guess) == 1
    i: int = 0
    while i < len(secret_word):
        if guess == secret_word[i]:
            return True
        else:
            i += 1
    return False

def emojified(guess: str, secret_word: str) -> str:
    """Returns white, yellow, or green boxes depending on the accuracy of the guess"""
    assert len(guess) == len(secret_word)
    result: str = ""
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == guess[i]:
            result += GREEN_BOX
        elif contains_char(secret_word, guess[i]) == True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX 
        i += 1
    return result

def input_guess(expected_length: int) -> str:
    """Returns a message asking for a word the length of the inputted integer"""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn: int = 0
    turn_limit: int = 6
    playing: bool = True
    while turn < turn_limit and playing == True:
        print(f"=== Turn {turn + 1}/{turn_limit} ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            print(f"You won in {turn + 1}/{turn_limit} turns!")
            playing = False
        else:
            turn += 1
        if turn == turn_limit:
            print(f"X/{turn_limit} - Sorry, try again tomorrow!")
        
if __name__ == "__main__":
    main()