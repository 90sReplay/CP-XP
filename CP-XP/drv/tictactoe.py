import random

board = {str(i): "-" for i in range(1, 10)}

winning_combinations = [
    ["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"],
    ["1", "4", "7"], ["2", "5", "8"], ["3", "6", "9"],
    ["1", "5", "9"], ["3", "5", "7"]
]

def print_board():
    print(f"{board['1']} {board['2']} {board['3']}")
    print(f"{board['4']} {board['5']} {board['6']}")
    print(f"{board['7']} {board['8']} {board['9']}")

def check_win(player):
    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True
    return False

print_board()
tic = input("Choose a position (1 to 9): ")

while True:
    if tic in board:
        if board[tic] == "X":
            print("You already placed there.")
        elif board[tic] == "O":
            print("There's an O there.")
        else:
            board[tic] = "X"
            if check_win("X"):
                print_board()
                input("Congrats, you win! Press Enter to quit.")
                break

            empty_positions = [key for key, value in board.items() if value == "-"]
            if empty_positions:
                ranv = random.choice(empty_positions)
                board[ranv] = "O"
                if check_win("O"):
                    print_board()
                    input("The computer wins! Press Enter to quit.")
                    break

            print_board()  

    else:
        print("?Syntax Error")

    tic = input("Choose a position (1 to 9): ")
