import random

# Welcome Message
print("👩‍🏫 Welcome to the 'Guess the Number' EdTech Game! 🎮")
print("\n📚 Instructions:")
print("1️⃣ The computer will randomly select a number between 1 and 50.")
print("2️⃣ Your job is to guess the number! You'll get hints if you're wrong.")
print("3️⃣ If you enter a number outside the range, you'll see a warning.")
print("4️⃣ Type 'exit' anytime to quit the game.")
print("5️⃣ See how many tries it takes you to guess the correct number. Let's go!\n")

# Start the game
while True:
    # Generate a random number between 1 and 50
    target_number = random.randint(1, 50)
    attempts = 0  # Count the number of attempts

    print("🤖 The computer has picked a number between 1 and 50.")
    print("Try to guess it! Type your guess below:\n")

    while True:
        # Get user input
        user_input = input("Enter your guess (or type 'exit' to quit): ").lower()

        # Exit condition
        if user_input == "exit":
            print("\n👋 Thanks for playing! See you next time!")
            exit()

        # Validate input
        if not user_input.isdigit():
            print("⚠️ Invalid input! Please enter a number between 1 and 50.")
            continue

        # Convert input to an integer
        user_guess = int(user_input)

        # Check for out-of-range guesses
        if user_guess < 1 or user_guess > 50:
            print("❌ Out of range! Please guess a number between 1 and 50.")
            continue

        # Increment attempts
        attempts += 1

        # Check the guess
        if user_guess < target_number:
            print("🔼 Too low! Try again.")
        elif user_guess > target_number:
            print("🔽 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed the number {target_number} in {attempts} attempts.")
            break

    # Play again prompt
    play_again = input("\n🔄 Would you like to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\n👋 Thanks for playing! Keep learning and have a great day!")
        break
