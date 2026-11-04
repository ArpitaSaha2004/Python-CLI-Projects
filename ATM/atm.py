
balance = 0

def show_menu():
    print("\n" + "=" * 35)
    print("          🏦 PYTHON ATM")
    print("=" * 35)
    print("  1. Check Balance")
    print("  2. Deposit Amount")
    print("  3. Withdraw Amount")
    print("  4. Exit")
    print("=" * 35)


def check_balance():
    print(f"\nYour current balance: ₹{balance:,}")

def deposit():
    global balance
    try:
        amount = int(input("\nEnter deposit amount: ₹"))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        else:
            balance += amount
            print(f"₹{amount:,} deposited successfully!")
            print(f"Available balance: ₹{balance:,}")

    except ValueError:
        print("Invalid input! Please enter a number.")


def withdraw():
    global balance
    try:
        amount = int(input("\nEnter withdrawal amount: ₹"))
        if amount <= 0:
            print("Please enter an amount greater than zero.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            print(f"₹{amount:,} withdrawn successfully!")
            print(f"Available balance: ₹{balance:,}")

    except ValueError:
        print("Invalid input! Please enter a number.")

while True:
    show_menu()
    try:
        choice = int(input("\nEnter your choice (1-4): "))
        if choice == 1:
            check_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            print("\nThank you for using Python ATM!")
            print("Have a nice day! 👋")
            break
        else:
            print("Invalid choice! Please select 1-4.")
    except ValueError:
        print("Please enter a valid number.")
