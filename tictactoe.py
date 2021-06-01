import pyfiglet


board = {}

win_x = 0
win_o = 0

namex=input("What is your name player X=>")
nameo=input("What is your name player O=>")
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')


def print_winner(name):
    ascii_banner = pyfiglet.figlet_format(F"{name} is winner")
    print(ascii_banner)

for i in range(1, 10):
    board[i] = str(i)

def print_tictac(board):
    print(chr(27) + '[2j')
    print('\033c')
    print('\x1bc')
    ascii_banner = pyfiglet.figlet_format(F" {board[1]} | {board[2]} | {board[3]}")
    print (ascii_banner)
    ascii_banner = pyfiglet.figlet_format("____________")
    print(ascii_banner)
    ascii_banner = pyfiglet.figlet_format(F" {board[4]} | {board[5]} | {board[6]}")
    print(ascii_banner)
    ascii_banner = pyfiglet.figlet_format("____________")
    print(ascii_banner)
    ascii_banner = pyfiglet.figlet_format(F" {board[7]} | {board[8]} | {board[9]}")
    print(ascii_banner)

def check_trio(board, value, a, b, c):
    if board[a] == value and board[b] == value and board[c] == value:
        return True
    else:
        return False

def check_winner_X(board):
    if (
            check_trio(board, "X", 1, 2, 3) or
            check_trio(board, "X", 4, 5, 6) or
            check_trio(board, "X", 7, 8, 9) or
            check_trio(board, "X", 1, 4, 7) or
            check_trio(board, "X", 2, 5, 8) or
            check_trio(board, "X", 3, 6, 9) or
            check_trio(board, "X", 1, 5, 9) or
            check_trio(board, "X", 3, 5, 7)

    ):
        return True
    else:
        return False


def check_winner_O(board):
    if (
            check_trio(board, "O", 1, 2, 3) or
            check_trio(board, "O", 4, 5, 6) or
            check_trio(board, "O", 7, 8, 9) or
            check_trio(board, "O", 1, 4, 7) or
            check_trio(board, "O", 2, 5, 8) or
            check_trio(board, "O", 3, 6, 9) or
            check_trio(board, "O", 1, 5, 9) or
            check_trio(board, "O", 3, 5, 7)

    ):
        return True
    else:
        return False



game_end = False

print_tictac(board)
while game_end == False:
    while True:
        user1 = input(F"{namex}- Where do you want to place =>")
        user1 = int(user1)

        if board[user1] == "X" or board[user1] == "O":
            print(" Invalid Choice !")
            continue
        else:
            board[user1] = "X"
            if check_winner_X(board)==True:
                win_x= win_x+1
                print  (F"{namex} is winner")
                game_end = True
                print_winner(namex)
            break

    if game_end == False:
        print_tictac(board)
    if game_end == True:
        break
    while True:
        user2 = input(F"{nameo}- Where do you want to place =>")
        user2 = int(user2)
        if board[user2] == "X" or board[user2] == "O":
            print(" Invalid Choice !")
            continue
        else:
            board[user2] = "O"
            if check_winner_O(board)==True:
                win_o= win_o+1
                print  (F"{nameo} is winner")
                game_end = True
                print_winner(nameo)
            break
    if game_end == False:
        print_tictac(board)











