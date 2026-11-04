import random

choices = ["rock", "paper", "scissors"]


def welcome():
    print("\n" + "=" * 40)
    print("          ROCK PAPER SCISSORS")
    print("              THE GAME")
    print("=" * 40)


def get_player_choice():
    while True:
        player = input("\nChoose (rock/paper/scissors): ").lower()

        if player in choices:
            return player

        print("Invalid choice! Please try again.")

def get_computer_choice():
    return random.choice(choices)

def check_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "player"
    else:
        return "computer"

def display_score(player_score, computer_score, draws):
    print("\n" + "-" * 35)
    print("             SCOREBOARD")
    print("-" * 35)
    print(f"     Player   : {player_score}")
    print(f"     Computer : {computer_score}")
    print(f"     Draws    : {draws}")
    print("-" * 35)

def play_game():
    player_score = 0
    computer_score = 0
    draws = 0
    print("\nFirst to win 3 rounds wins the game!")
    round_number = 1
    while player_score < 3 and computer_score < 3:

        print(f"\n========== ROUND {round_number} ==========")

        player = get_player_choice()
        computer = get_computer_choice()
        print("\nYour choice     :", player)
        print("Computer choice :", computer)
        result = check_winner(player, computer)
        if result == "player":
            print("\nCongratulations! You won this round.")
            player_score += 1
        elif result == "computer":
            print("\nComputer won this round.")
            computer_score += 1
        else:
            print("\nIt's a draw!")
            draws += 1
        display_score(player_score, computer_score, draws)
        round_number += 1

    print("\n" + "=" * 40)
    print("             FINAL RESULT")
    print("=" * 40)

    if player_score == 3:
        print("Congratulations! You won the game!")

    else:
        print("Computer won the game! Better luck next time.")

    print(f"\nFinal Score: {player_score} - {computer_score}")
    print(f"Total Draws: {draws}")
    print("=" * 40)

def main():
    welcome()
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThank you for playing!")
            print("See you again!")
            break

main()