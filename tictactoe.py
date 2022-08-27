def drawboard(board):

    print (f"| {board6}  |  {board7}  |  {board8} |")

    print ('---------------')

    print (f"| {board3}  |  {board4}  |  {board5} |")

    print('-----------------')

    print (f"| {board0}  |  {board1}  |  {board2} |")

def player1_input():
    global board0, board1, board2, board3, board4, board5, board6, board7, board8
    print("Player 1 moves")
    x = int(input("How far right: "))
    y = int(input("How far down: "))

    if x == 1 and y == 1 and board6 != "x" and board6 != "y":
        board6 = "x"
    elif x == 2 and y == 1 and board7 != "x" and board7 != "y":
        board7 = "x"
    elif x == 3 and y == 1 and board8 != "x" and board8 != "y":
        board8 = "x"
    elif x == 1 and y == 2 and board3 != "x" and board3 != "y":
        board3 = "x"
    elif x == 2 and y == 2 and board4 != "x" and board4 != "y":
        board4 = "x"
    elif x == 3 and y == 2 and board5 != "x" and board5 != "y":
        board5 = "x"
    elif x == 1 and y == 3 and board0 != "x" and board0 != "y":
        board0 = "x"
    elif x == 2 and y == 3 and board1 != "x" and board1 != "y":
        board1 = "x"
    elif x == 3 and y == 3 and board2 != "x" and board2 != "y":
        board2 = "x"
    else:
        print("Please pick an open spot")
        drawboard([board0, board1, board2, board3, board4, board5, board6, board7, board8])
        player1_input()

def player2_input():
    global board0, board1, board2, board3, board4, board5, board6, board7, board8
    print("Player 2 moves")
    x = int(input("How far right: "))
    y = int(input("How far down: "))

    if x == 1 and y == 1 and board6 != "x" and board6 != "y":
        board6 = "y"
    elif x == 2 and y == 1 and board7 != "x" and board7 != "y":
        board7 = "y"
    elif x == 3 and y == 1 and board8 != "x" and board8 != "y":
        board8 = "y"
    elif x == 1 and y == 2 and board3 != "x" and board3 != "y":
        board3 = "y"
    elif x == 2 and y == 2 and board4 != "x" and board4 != "y":
        board4 = "y"
    elif x == 3 and y == 2 and board5 != "x" and board5 != "y":
        board5 = "y"
    elif x == 1 and y == 3 and board0 != "x" and board0 != "y":
        board0 = "y"
    elif x == 2 and y == 3 and board1 != "x" and board1 != "y":
        board1 = "y"
    elif x == 3 and y == 3 and board2 != "x" and board2 != "y":
        board2 = "y"
    else:
        print("Please pick an open spot")
        drawboard([board0, board1, board2, board3, board4, board5, board6, board7, board8])
        player2_input()

def checkwin():
    global stoploop
    if board6 == "y" and board3 == "y" and board0 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board7 == "y" and board4 == "y" and board1 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board8 == "y" and board5 == "y" and board2 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board6 == "y" and board7 == "y" and board8 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board3 == "y" and board4 == "y" and board5 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board0 == "y" and board1 == "y" and board2 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board6 == "y" and board4 == "y" and board2 == "y":
        print("Player 2 wins!")
        stoploop = 1
    if board8 == "y" and board4 == "y" and board0 == "y":
        print("Player 2 wins!")
        stoploop = 1


    if board6 == "x" and board3 == "x" and board0 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board7 == "x" and board4 == "x" and board1 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board8 == "x" and board5 == "x" and board2 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board6 == "x" and board7 == "x" and board8 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board3 == "x" and board4 == "x" and board5 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board0 == "x" and board1 == "x" and board2 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board6 == "x" and board4 == "x" and board2 == "x":
        print("Player 1 wins!")
        stoploop = 1
    if board8 == "x" and board4 == "x" and board0 == "x":
        print("Player 1 wins!")
        stoploop = 1

board0 = "0"
board1 = "0"
board2 = "0"
board3 = "0"
board4 = "0"
board5 = "0"
board6 = "0"
board7 = "0"
board8 = "0"
stoploop = 0

drawboard([board0, board1, board2, board3, board4, board5, board6, board7, board8])

while checkwin != 0:
    player1_input()
    drawboard([board0, board1, board2, board3, board4, board5, board6, board7, board8])
    checkwin()
    if stoploop == 1:
        break
    if board0 != "0" and board1 != "0" and board2 != "0" and board3 != "0" and board4 != "0" and board5 != "0" and board6 != "0" and board7 != "0" and board8 != "0":
        print("There are no moves left, Tie game!")
        break
    player2_input()
    drawboard([board0, board1, board2, board3, board4, board5, board6, board7, board8])
    checkwin()
    if stoploop == 1:
        break
    if board0 != "0" and board1 != "0" and board2 != "0" and board3 != "0" and board4 != "0" and board5 != "0" and board6 != "0" and board7 != "0" and board8 != "0":
        print("There are no moves left, Tie game!")
        break