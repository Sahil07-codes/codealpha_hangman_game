import random

def hangman():
    words = ["python", "github", "hangman", "computer", "science"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    tries = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while tries > 0 and "_" in guessed:
        print("Word:", " ".join(guessed))
        print(f"Tries left: {tries}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Already guessed.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i, char in enumerate(word):
                if char == guess:
                    guessed[i] = guess
        else:
            tries -= 1
            print("Wrong guess!")

    if "_" not in guessed:
        print("You won! The word was:", word)
    else:
        print("You lost! The word was:", word)

if __name__ == "__main__":
    hangman()
