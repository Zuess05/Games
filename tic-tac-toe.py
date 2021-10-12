board = [" " for x in range(10)]


def choice(letter,pos):
    board[pos]=letter

def isBoardFree(pos):
    return board[pos]==" "

def printBoard(board):
    print('   ' +"|" + "   "+ "|" + "   " )
    print(" " + board[1] + " | " + board[2] + " | " + board[3] )
    print('   ' +"|" + "   "+ "|" + "   " )
    print("------------")
    print('   ' +"|" + "   "+ "|" + "   " )
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print('   ' +"|" + "   "+ "|" + "   " )
    print("------------")
    print('   ' +"|" + "   "+ "|" + "   " )
    print(" " + board[7] + " | " + board[8] + " | " + board[9] )
    print('   ' +"|" + "   "+ "|" + "   " )

def isBoardFUll(board):
    if board.count(" ")>1:
        return False
    else:
        return True

def winner(b,l):
    return ((b[1]==l and b[2]==l and b[3]==l) or (b[4]==l and b[5]==l and b[6]==l) or (b[7]==l and b[8]==l and b[9]==l) or (b[1]==l and b[5]==l and b[9]==l) or (b[3]==l and b[5]==l and b[7]==l) or (b[1]==l and b[4]==l and b[7]==l) or (b[2]==l and b[5]==l and b[8]==l) or (b[3]==l and b[6]==l and b[9]==l))

def playerMove():
    run = True
    while run:
        turn = (input("Select a position to place 'X' (1-9)"))
        try:
            turn = int(turn)
            if turn > 0  and turn < 10:
                if isBoardFree(turn):
                    run = False
                    choice("X",turn)
                else:
                    print("There is a letter already present in that location")
            else:
                print("Invalid choice\n Please enter a number between 1 and 9")
        except:
            print("Please type a number")

def computerMove():
    possibleMove = [x for x,letter in enumerate(board) if letter == " " and x != 0]  #enumerate function gives all possible spaces in that parameter
    move = 0
    for item in ["O" , "X"]:
        for i in possibleMove:
            boardcpy = board[:]
            boardcpy[i] = item
            if winner(boardcpy,item):
                move = i
                return move

    corners = []            #this is to check if corner places are empty and for it to make a move
    for i in possibleMove:
        if i in [1,3,7,9]:
            corners.append(i)
    if len(corners)>0:
        move = selectRandom(corners)
        return move

    if 5 in possibleMove:       #to check if the middle box is free
        move = 5
        return move

    edges = []
    for i in possibleMove:    # to check for other remaining boxes
        if i in [2,4,6,8]:
            edges.append(i)
    if len(edges)>0:
        move = selectRandom(edges)
        return move

def selectRandom(a):
    import random
    ln = len(a)
    r = random.randrange(0,ln)
    return a[r]

def main():
    print("Welcome to tic-tac-toe")
    printBoard(board)
    while not(isBoardFUll(board)):
        if not(winner(board,"O")):
            playerMove()
            printBoard(board)
        else:
            print("You lost the game!")
            break
        if not(winner(board,"X")):
            move = computerMove()
            if move==0:
                print(" ")
            else:
                choice("O", move)
                print("Computer made a move at pos:",move)
                printBoard(board)
        else:
            print("You WIN!!!")
            break
    if isBoardFUll(board):
        print("Tie-Game!")

while True:
    x = input('Do you want to play?\n (y/n)')
    if x.lower() == "y":
        board = [" " for x in range(10)]
        print("_____________")
        main()
    else:
        break
