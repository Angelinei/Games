import random

def roll_dice(sides):
    """
    Rolls a dice with the given number of sides.
    :param sides: int - Number of sides on the dice.
    :return: int - A random result from 1 to sides.
    """
    return random.randint(1, sides)

def infinity_dice():
    """
    Infinity Dice interactive function.
    Rolls a dice of any size repeatedly based on user input.
    """
    print("🎲 Welcome to Infinity Dice! 🎲")
    
    while True:
        try:
            sides = int(input("How many sides?: "))
            if sides <= 0:
                print("Please enter a number greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
        
        while True:
            result = roll_dice(sides)
            print(f"You rolled: {result}")
            
            roll_again = input("Roll again? (yes/no): ").strip().lower()
            if roll_again not in ['yes', 'y']:
                print("Thanks for playing Infinity Dice! 🎲")
                return

# Start the game
if __name__ == "__main__":
    infinity_dice()
