import random

def draw_hangman(mistakes):
    stages = [
        """\n         +---+\n             |\n             |\n             |\n            ===\n        """,
        """\n         +---+\n         O   |\n             |\n             |\n            ===\n        """,
        """\n         +---+\n         O   |\n         |   |\n             |\n            ===\n        """,
        """\n         +---+\n         O   |\n        /|   |\n             |\n            ===\n        """,
        """\n         +---+\n         O   |\n        /|\\  |\n             |\n            ===\n        """,
        """\n         +---+\n         O   |\n        /|\\  |\n        /    |\n            ===\n        """,
        """\n         +---+\n         O   |\n        /|\\  |\n        / \\  |\n            ===\n        """
    ]
    return stages[mistakes]

def play_hangman():
    # Word list
    words = ["python", "challenge", "hangman", "developer", "programming", "debugging"]
    word = random.choice(words).lower()
    
    guessed_word = ["_" for _ in word]
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman! Try to guess the word, one letter at a time.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print("\n" + draw_hangman(incorrect_guesses))
        print("Word: ", " ".join(guessed_word))
        print("Guessed letters: ", ", ".join(sorted(guessed_letters)))

        # Get user input
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            for i, letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            print(f"Sorry, the letter '{guess}' is not in the word.")
            incorrect_guesses += 1

        if "_" not in guessed_word:
            print("\n" + draw_hangman(incorrect_guesses))
            print("Congratulations! You've guessed the word: ", word)
            break
    else:
        print("\n" + draw_hangman(incorrect_guesses))
        print(f"Game over! The word was '{word}'. Better luck next time!")

if __name__ == "__main__":
    play_hangman()
