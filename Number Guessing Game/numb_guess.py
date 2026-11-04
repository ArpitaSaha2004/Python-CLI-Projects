
import random

def play_game():

    number = random.randint(1, 20)
    no_of_guesses = 0

    lower = 1
    higher = 20

    print("\n" + "=" * 40)
    print("          🎯 NUMBER GUESSING GAME")
    print("=" * 40)
    print(f"I'm thinking of a number between {lower} and {higher}.")
    print("Can you guess it?")
    print("=" * 40)

    while True:
        try:
            guess = int(input("\nEnter your guess: "))

            if guess < lower or guess > higher:
                print(f"Please guess between {lower} and {higher}!")
                continue

            no_of_guesses += 1

            if guess == number:
                print("\nCORRECT! You guessed the number!")
                break

            elif guess < number:
                diff = number - guess
                print(f"Too low! You are {diff} away from the number.")

            else:
                diff = guess - number
                print(f"Too high! You are {diff} away from the number.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print("\n" + "-" * 40)
    print(f"The correct number was: {number}")
    print(f"Total attempts: {no_of_guesses}")
    print("-" * 40)


while True:
    play_game()
    choice = input("\nWould you like to play again? (yes/no): ").lower().strip()
    if choice not in ("yes", "y"):
        print("\nThanks for playing! Goodbye! 👋")
        break
