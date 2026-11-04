
def display_board(board):
    print("\n========== TIC TAC TOE ==========")

    for row in board:
        print(" | ".join(row))
        print("-" * 11)

def check_winner(board):

    for row in board:
        if row[0] == row[1] == row[2]:
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def check_draw(board):

    for row in board:
        for cell in row:
            if cell not in ["X", "Y"]:
                return False
    return True

def play_game():

    board = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]

    current_player = "X"

    while True:
        display_board(board)

        while True:
            try:
                position = int(input(
                    f"\nPlayer {current_player}, choose a position (1-9): "
                ))

                if position < 1 or position > 9:
                    print("Please enter a number between 1 and 9.")
                    continue
                row = (position - 1) // 3
                col = (position - 1) % 3
                if board[row][col] in ["X", "Y"]:
                    print("Position already occupied! Try again.")
                    continue
                break
            except ValueError:
                print("Invalid input! Enter a number.")

        board[row][col] = current_player

        winner = check_winner(board)

        if winner:
            display_board(board)
            print(f"\nCongratulations! Player {winner} wins!")
            break

        if check_draw(board):
            display_board(board)
            print("\nIt's a draw! Nobody wins.")
            break

        if current_player == "X":
            current_player = "Y"
        else:
            current_player = "X"

def main():
    print("\nWelcome to Tic Tac Toe!")
    while True:
        play_game()
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again != "yes":
            print("\nThanks for playing!")
            break
main()
