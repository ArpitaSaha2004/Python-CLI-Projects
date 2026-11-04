
import random

FRUITS = ["APPLE", "MANGO", "WATERMELON", "GRAPES", "LEMON"]

PAYOUTS = {
    "APPLE": 2,
    "MANGO": 3,
    "WATERMELON": 4,
    "GRAPES": 10,
    "LEMON": 20
}

INITIAL_BALANCE = 100

def spin():
    return [random.choice(FRUITS) for _ in range(3)]


def print_row(row):

    print("\n +--------------------------------+")
    print(" |          SPIN RESULT           |")
    print(" +--------------------------------+")
    print(f" |  {row[0]:<10} | {row[1]:<10} | {row[2]:<10} |")
    print(" +--------------------------------+")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        multiplier = PAYOUTS[row[0]]
        return bet * multiplier
    return 0

def show_payouts():
    print("\n========== PAYOUT TABLE ==========")
    for fruit, multiplier in PAYOUTS.items():
        print(f"{fruit:<15} : {multiplier}x your bet")
    print("==================================")

def get_bet(balance):
    while True:
        bet = input(
            "\nPlace your bet (or enter Q to quit): "
        ).strip().lower()
        if bet == "q":
            return None
        if not bet.isdigit():
            print("Please enter a valid whole number.")
            continue
        bet = int(bet)
        if bet <= 0:
            print("Bet must be greater than zero.")
            continue
        if bet > balance:
            print("Insufficient balance.")
            continue
        return bet

def play_game():
    balance = INITIAL_BALANCE
    rounds_played = 0
    total_winnings = 0
    total_losses = 0
    print("\n====================================")
    print("          WELCOME TO SPIN GAME")
    print("====================================")
    print("Available fruits:", ", ".join(FRUITS))
    show_payouts()

    while balance > 0:
        print(f"\nCurrent balance: ${balance}")
        bet = get_bet(balance)
        if bet is None:
            break
        
        balance -= bet

        row = spin()

        print("\nSpinning...")
        print_row(row)

        payout = get_payout(row, bet)
        rounds_played += 1

        if payout > 0:
            print("\nCongratulations! You won!")
            print(f"Your payout: ${payout}")
            print(f"Profit this round: ${payout - bet}")
            balance += payout
            total_winnings += payout - bet
        else:
            print("\nSorry! No matching fruits.")
            print(f"You lost: ${bet}")
            total_losses += bet
        print(f"Updated balance: ${balance}")
        if balance <= 0:
            print("\nYou have run out of balance.")
            break

        while True:

            play_again = input(
                "\nDo you want to play again? (Y/N): "
            ).strip().lower()

            if play_again in ["y", "n"]:
                break

            print("Please enter Y or N.")

        if play_again == "n":
            break


    print("\n====================================")
    print("             GAME SUMMARY")
    print("====================================")

    print(f"Initial balance : ${INITIAL_BALANCE}")
    print(f"Final balance   : ${balance}")
    print(f"Rounds played   : {rounds_played}")
    print(f"Total winnings  : ${total_winnings}")
    print(f"Total losses    : ${total_losses}")

    net_result = balance - INITIAL_BALANCE

    if net_result > 0:
        print(f"Net profit      : ${net_result}")

    elif net_result < 0:
        print(f"Net loss        : ${abs(net_result)}")

    else:
        print("Result          : Break even")

    print("====================================")
    print("          THANK YOU FOR PLAYING")
    print("====================================")


if __name__ == "__main__":
    play_game()
