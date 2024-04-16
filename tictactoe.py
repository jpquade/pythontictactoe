import random

# Player random player selected first
player = bool(random.getrandbits(1))

# Score Keeping
scoreCol = [0,0,0]
scoreRow = [0,0,0]
scoreDiag = 0
scoreAntiDiag = 0

# Number of rows and columns in the tic tac board
r, c = (3, 3)

# Create 3 x 3 tic tac toe board
board = [['. ' for x in range(r)] for y in range(c)]

# Column and Row Number Selected
numberCol = 0
numberRow = 0

# First attempt at entering row column
def firstEntry():
    
    global numberRow    
    tempNumber = input("Enter row number: ")
    numberRow = numberTable(tempNumber) - 1

    global numberCol
    tempNumber = input("Enter column number: ") 
    numberCol= numberTable(tempNumber) - 1
    
# Takes entries from user that need to be in-between (1-3) and returns valid entry
def numberTable(number):
    
    while(not(number.isnumeric()) or (int(number) < 1 or 3 < int(number))):
        
        if(number.isnumeric()):
            
            if(int(number) < 1 or 3 < int(number)):
                print("Entry needs to be in-between 1 and 3")
                number = input("Enter column number: ")     
        else:
            print("Entry is not a number and needs to be in-between 1 and 3")
            number = input("Enter column number: ")    

    number = int(number)
    
    return number

# Looks for empty spot to insert x or o
def findEmptySpot():
    while(board[numberRow][numberCol] != '. '):
        
        printBoard()
    
        print("Please enter a valid unused position")
        
        firstEntry()

# Prints current board
def printBoard():
    
    global board

    print()
    print(board[0])
    print(board[1])
    print(board[2])
    print()
    
# Main Program of starting game
while True:
    
    if(player):
        print("\nPlayer X's turn")
    else:
        print("\nPlayer O's turn")
    
    firstEntry()
    findEmptySpot()

    token = "X" if(player) else "O"
    
    board[numberRow][numberCol] = token
    
    # Processes scoring according to column, row, diagonal, antidiagonal
    scoreCol[numberCol] = scoreCol[numberCol] + 1 if player else scoreCol[numberCol] - 1
    scoreRow[numberRow] = scoreRow[numberRow] + 1 if player else scoreRow[numberRow] - 1
    if(numberCol == numberRow):
        scoreDiag = scoreDiag + 1 if player else scoreDiag - 1
    if(numberCol + 1 + numberRow + 1 == 4):
        scoreAntiDiag = scoreAntiDiag + 1 if player else scoreAntiDiag - 1
  
    printBoard()
    
    # Checks if a player wins: row, col, diagonal, antidiagonal according to the number 3
    if(abs(scoreCol[numberCol]) == 3 or abs(scoreRow[numberRow]) == 3 or abs(scoreDiag) == 3 or abs(scoreAntiDiag) == 3):
        print("Player:", token, "wins!")
        break
    
    # Changes player after turn
    player = not(player)