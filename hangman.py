"""CodeAlpha Task 1: Console Hangman game."""
import random

WORDS = ["python", "planet", "garden", "rocket", "silver"]
MAX_WRONG = 6

def play():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0
    print("Welcome to Hangman! Guess the hidden word.")
    while wrong < MAX_WRONG:
        print("\nWord:", " ".join(c if c in guessed else "_" for c in word))
        print(f"Wrong guesses remaining: {MAX_WRONG - wrong}")
        guess = input("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.")
            continue
        if guess in guessed:
            print("You already guessed that letter.")
            continue
        guessed.add(guess)
        if guess not in word:
            wrong += 1
            print("Incorrect guess!")
        if all(c in guessed for c in word):
            print(f"Congratulations! You guessed '{word}'!")
            return
    print(f"Game over! The word was '{word}'.")

if __name__ == "__main__":
    play()
