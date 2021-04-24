def printboard(log):
    space = "\n"
    boardtop = " "+str(log[0]) + "   |   " + str(log[1]) + "   |   " + str(log[2])
    boardline = "___________________"
    boardmiddle = " " + str(log[3]) + "   |   " + str(log[4]) + "   |   " + str(log[5])
    boardbottom = " " + str(log[6]) + "   |   " + str(log[7]) + "   |   " + str(log[8])
    print(space)
    print(space)
    print(space)
    print(space)
    print(boardtop)
    print(boardline)
    print(boardmiddle)
    print(boardline)
    print(boardbottom)

playerstatus = 1
log = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def wincheck(player, log):
    if log[0] == player and log[1] == player and log[2] == player:
        return True

    if log[3] == player and log[4] == player and log[5] == player:
        return True

    if log[6] == player and log[7] == player and log[8] == player:
        return True

    if log[0] == player and log[3] == player and log[6] == player:
        return True

    if log[1] == player and log[4] == player and log[7] == player:
        return True

    if log[2] == player and log[5] == player and log[8] == player:
        return True

    if log[2] == player and log[5] == player and log[8] == player:
        return True

    if log[0] == player and log[4] == player and log[8] == player:
        return True

    if log[6] == player and log[4] == player and log[2] == player:
        return True



def compsmove(log):
    possibleMoves = []
    for i in range(9):
        if log[i] != "X" and log[i] != "O":
            possibleMoves.append(log[i])

    moves = 0
    for let in ["O", "X"]:
        for i in possibleMoves:
            logcopy = log[:]
            logcopy[int(i - 1)] = let
            if wincheck(let, logcopy):
                moves = int(i)
                return moves


    if 5 in possibleMoves:
        moves = 5
        return moves

    cornersopen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)

    if len(cornersopen) > 0:
        moves = selectrandom(cornersopen)
        return moves


    edgesopen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesopen.append(i)

    if len(edgesopen) > 0:
        moves = selectrandom(edgesopen)

    return moves

def selectrandom(list):
    import random
    ln = len(list)
    r = random.randrange(0, ln)
    return list[r]

printboard(log)
input_var = "something"
move = 0
while move < 9:
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
        printboard(log)
        if wincheck("X", log) == True:
            print("Player 1 won!!")
            exit()
        move = move + 1
    else:
        compmove = compsmove(log)
        playerstatus = 1
        log[int(compmove - 1 )] = "O"
        printboard(log)
        if wincheck("O", log) == True:
            print("Computer won!!")
            exit()
        print("Computer played " + str(compmove))
        move = move + 1

print("Its a draw!!!!")