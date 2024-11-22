from getpass import getpass

print("🎉 E P I C    🪨  📄 ✂️    B A T T L E 🎉")
print("\nWelcome to Rock, Paper, Scissors!")
print("Two warriors enter the arena! Prepare for the ultimate showdown! ⚔️\n")

# Get player names
player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

# Function to validate player moves
def get_valid_move(player_name):
    while True:
        move = getpass(f"{player_name}, enter your move (R, P, S): ").strip().upper()
        if move in ['R', 'P', 'S']:
            return move
        print("Invalid input! Please type 'R', 'P', or 'S'. Try again!")

# Function to determine the winner of a round
def determine_winner(player1_move, player2_move):
    if player1_move == player2_move:
        return "tie"
    elif (player1_move == "R" and player2_move == "S") or \
         (player1_move == "S" and player2_move == "P") or \
         (player1_move == "P" and player2_move == "R"):
        return "player1"
    else:
        return "player2"

# Main game loop
while True:
    print("\n--- Starting a New 3-Round Game ---")
    
    player1_score = 0
    player2_score = 0
    rounds = 3

    for round_number in range(1, rounds + 1):
        print(f"\n--- Round {round_number} ---")
        player1_move = get_valid_move(player1_name)
        player2_move = get_valid_move(player2_name)
        winner = determine_winner(player1_move, player2_move)

        if winner == "tie":
            print("It's a tie for this round! 🤝")
        elif winner == "player1":
            print(f"{player1_name} wins this round! 🎉")
            player1_score += 1
        else:
            print(f"{player2_name} wins this round! 🎉")
            player2_score += 1

        print(f"Current Score: {player1_name} {player1_score} - {player2_score} {player2_name}")

    # Announce the final winner
    print("\n--- Final Results ---")
    if player1_score > player2_score:
        print(f"{player1_name} is the champion! 🏆")
    elif player2_score > player1_score:
        print(f"{player2_name} is the champion! 🏆")
    else:
        print("It's an epic draw! 🤝")

    # Ask if players want to play again
    play_again = input("\nDo you want to play another 3-round game? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("\nThanks for playing! See you next time! 🎮")
        break
