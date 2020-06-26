print("DEMO BOARD = ")

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

game_is_still_going = True
winner = None
current_player = "X"


def play_game():
    display_board()

    while game_is_still_going:
        handel_turn(current_player)

        check_game_is_over()

        flip_player()

    if winner == "X" or winner == "0":
        print(" ")
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


def display_board():
    print(board[6] + "|" + board[7] + "|" + board[8] + "     7 | 8 | 9")
    print(board[3] + "|" + board[4] + "|" + board[5] + "     4 | 5 | 6")
    print(board[0] + "|" + board[1] + "|" + board[2] + "     1 | 2 | 3")



def handel_turn(player):
    print(player + " s turn.")
    position = input("choose position from 1-9:")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("choose position from 1-9:")
        position = int(position) - 1
        if board[position] == "_":
            valid = True
        else:
            print("You cant go there . Go again")
    board[position] = player
    display_board()


def check_game_is_over():
    check_for_win()
    check_if_tie()


def check_for_win():
    global winner

    row_winner = check_row()

    colom_winner = check_colom()

    diagonal_winner = check_diagonal()

    if row_winner:
        winner = row_winner

    elif colom_winner:
        winner = colom_winner

    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None



def check_row():
    global game_is_still_going
    row1 = board[0] == board[1] == board[2] != "_"
    row2 = board[3] == board[4] == board[5] != "_"
    row3 = board[6] == board[7] == board[8] != "_"

    if row1 or row2 or row3:
        game_is_still_going = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None


def check_colom():
    global game_is_still_going
    col1 = board[0] == board[3] == board[6] != "_"
    col2 = board[1] == board[4] == board[7] != "_"
    col3 = board[2] == board[5] == board[8] != "_"

    if col1 or col2 or col3:
        game_is_still_going = False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None


def check_diagonal():
    global game_is_still_going
    dia1 = board[0] == board[4] == board[8] != "_"
    dia2 = board[2] == board[4] == board[6] != "_"

    if dia1 or dia2:
        game_is_still_going = False
    if dia1:
        return board[0]
    elif dia2:
        return board[2]
    else:
        return None



def check_if_tie():
    global game_is_still_going
    if "_" not in board:
        game_is_still_going = False
        return True
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "0"
    elif current_player == "0":
        current_player = "X"

play_game()
