import os
def printboard(log):
    boardtop = " "+str(log[0]) + "   |   " + str(log[1]) + "   |   " + str(log[2])
    boardline = "___________________"
    boardmiddle = " " + str(log[3]) + "   |   " + str(log[4]) + "   |   " + str(log[5])
    boardbottom = " " + str(log[6]) + "   |   " + str(log[7]) + "   |   " + str(log[8])
    print(boardtop)
    print(boardline)
    print(boardmiddle)
    print(boardline)
    print(boardbottom)



playerstatus = 1
log = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def wincheck(player):
    if log[0] == player and log[1] == player and log[2] == player:
        print("player " + player + " wins!")
        exit()
    if log[3] == player and log[4] == player and log[5] == player:
        print("player " + player + " wins!")
        exit()
    if log[6] == player and log[7] == player and log[8] == player:
        print("player " + player + " wins!")
        exit()
    if log[0] == player and log[3] == player and log[6] == player:
        print("player " + player + " wins!")
        exit()
    if log[1] == player and log[4] == player and log[7] == player:
        print("player " + player + " wins!")
        exit()
    if log[2] == player and log[5] == player and log[8] == player:
        print("player " + player + " wins!")
        exit()
    if log[2] == player and log[5] == player and log[8] == player:
        print("player " + player + " wins!")
        exit()
    if log[0] == player and log[4] == player and log[8] == player:
        print("player " + player + " wins!")
        exit()
    if log[6] == player and log[4] == player and log[2] == player:
        print("player " + player + " wins!")
        exit()
printboard(log)
input_var = "something"

for i in range(9):
    if playerstatus == 1:
        input_var = input("PLAYER 1 where would you like to play --")
        if not input_var.isdigit() or int(input_var) < 1 or int(input_var) > 9:
            print("invalid value, try again")
            continue
        if log[int(input_var) - 1] == "X" or log[int(input_var) - 1] == "O":
            print("somehing has already been placed here try again.")
            continue

        log[int(input_var) - 1 ] = "X"
        playerstatus = 2
        wincheck("X")
        printboard(log)
    else:
        input_var = input("PLAYER 2 where would you like to play --")
        if not input_var.isdigit() or int(input_var) < 1 or int(input_var) > 9:
            print("invalid value, try again")
            continue
        if log[int(input_var) - 1] == "X" or log[int(input_var) -1 ] == "O":
            print("somehing has already been placed here try again.")
            continue
        log[int(input_var) - 1] = "O"
        playerstatus = 1
        wincheck("O")
        printboard(log)
print("the game is over, its a draw")

