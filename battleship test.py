from random import randint

board = []

for x in range(5):
    board.append(["0"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))
print("lets play battleship")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
print(ship_row)
print(ship_col)

for turn in range(4):
    print("turn",turn + 1)
    guess_row = int(input("Guess row:"))
    guess_col = int(input("Guess col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congrats you suck my battleship")
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("this number is not in the ocean")
        elif(board[guess_row][guess_col] == "X"):
            print("You already guessed that")
        else:
            print("You missed my battleship")
            board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game over")
        print_board(board)
