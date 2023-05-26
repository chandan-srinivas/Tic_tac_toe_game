import random
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
winner = None
currentplayer = "X"
gamerunning = True

#printing the gameboard

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take user input

def playerInput(board):
    i = int(input('Enter the position from 1-9: '))
    if i>=1 and i<=9 and board[i-1]=="-":
      board[i-1]=currentplayer
    else:
        print("The position is already filled ")


#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1]!="-":
       winner = board[0]
       return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner = board[6]
        return True

def checkrow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0]!="-":
        winner = board[0]
        return True
    elif board[1]==board[4]==board[7] and board[1]!="-":
        winner = board[1]
        return True
    elif board[2]==board[5]==board[8] and board[2]!="-":
        winner = board[2]
        return True 

def checkdiagnol(board):
    global winner
    if board[0]==board[4]==board[8] and board[0]!="-":
       winner = board[0]
       return True
    elif board[2]==board[4]==board[6] and board[2]!="-":
        winner = board[2]
        return True 

def checktie(board):
    global gamerunning
    if "-" not in board:
        printBoard(board)
        print("!   Tie   !")
        gamerunning = False

def checkWin():
    if checkdiagnol(board) or checkHorizontal(board) or checkrow(board):
       print(f"The final winner is {winner}")
       
#switch player
def switchplayer():
    global currentplayer
    if currentplayer =="X":
        currentplayer = "O"
    else:
        currentplayer = "X"

#computer

def computer(board):
    while currentplayer =="O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position]= "O"
            switchplayer()

#check whether win or tie again

while gamerunning:
      printBoard(board)
      playerInput(board)
      checkWin()
      checktie(board)
      switchplayer()
      computer(board)
      checkWin()
      checktie(board)      