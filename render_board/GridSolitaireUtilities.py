invalidTile = 'X'
ballTile = 'B'
emptyTile = '0'
startingBoard = [
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile],
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile],
    [ballTile,ballTile,ballTile,ballTile,ballTile,ballTile,ballTile],
    [ballTile,ballTile,ballTile,emptyTile,ballTile,ballTile,ballTile],
    [ballTile,ballTile,ballTile,ballTile,ballTile,ballTile,ballTile],
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile],
    [invalidTile,invalidTile,ballTile,ballTile,ballTile,invalidTile,invalidTile]]

solutionBoard = [
    [invalidTile,invalidTile,emptyTile,emptyTile,emptyTile,invalidTile,invalidTile],
    [invalidTile,invalidTile,emptyTile,emptyTile,emptyTile,invalidTile,invalidTile],
    [emptyTile,emptyTile,emptyTile,emptyTile,emptyTile,emptyTile,emptyTile],
    [emptyTile,emptyTile,emptyTile,ballTile,emptyTile,emptyTile,emptyTile],
    [emptyTile,emptyTile,emptyTile,emptyTile,emptyTile,emptyTile,emptyTile],
    [invalidTile,invalidTile,emptyTile,emptyTile,emptyTile,invalidTile,invalidTile],
    [invalidTile,invalidTile,emptyTile,emptyTile,emptyTile,invalidTile,invalidTile]]

def printBoard(board):
    for row in board:
        print(row)
    print()

def valueCopyBoard(board):
    newBoard = []
    for row in board:
        newBoard.append(row[:])
    return newBoard

def isSolution(board):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != solutionBoard[row][col]:
                return False
    return True

def generateLegalMovesForBoard(board):
    legalMoves = []
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == emptyTile: 
                legalMoves += generateLegalMovesForTile(board,row,col)
    return legalMoves

def generateLegalMovesForTile(board,row,col):
    moveList = []
    rowOffsets = [2,0,-2,0]
    rowJumpOffset = [1,0,-1,0]
    colOffsets = [0,-2,0,2]
    colJumpOffset = [0,-1,0,1]

    for i in range(len(rowOffsets)): # iterate through NSEW
        rowTarget = rowOffsets[i] + row
        colTarget = colOffsets[i] + col
        # If our spot we are looking at is on the board
        if rowTarget >= 0 and rowTarget < len(board) and colTarget >= 0 and colTarget < len(board):
            if board[rowTarget][colTarget] == ballTile:
                # There is a ball to jump
                if board[row+rowJumpOffset[i]][col+colJumpOffset[i]] == ballTile:
                    moveList.append([(rowTarget,colTarget),(row,col)])
    return moveList

# We trust the move is legal: therefore a ball moving into a non ball space
def getNewBoardWithMove(board,move):
    (rowSrc,colSrc) = move[0]
    (rowDst,colDst) = move[1]
    newBoard = valueCopyBoard(board)
    newBoard[rowDst][colDst] = ballTile
    newBoard[rowSrc][colSrc] = emptyTile
    # Calculate spot to eliminate
    if rowSrc != rowDst:
        eliminateRow = 1 if rowSrc < rowDst else -1
        newBoard[eliminateRow+rowSrc][colSrc] = emptyTile
    else:
        eliminateCol = 1 if colSrc < colDst else -1
        newBoard[rowSrc][eliminateCol+colSrc] = emptyTile
    return newBoard

def getSolution():
    initMoves = generateLegalMovesForBoard(startingBoard)
    for move in initMoves:
        result = getSolutionRecursive(startingBoard,[move])
        if result != None:
            return result
    return None

def getSolutionRecursive(boardOrg, moveList):
    lastMove = moveList[-1] # Grab the last move in the list
    currentBoard = getNewBoardWithMove(boardOrg,lastMove)
    if isSolution(currentBoard):
        return moveList
    currentMoves = generateLegalMovesForBoard(currentBoard)
    for move in currentMoves:
        localMoveList = moveList[:]
        localMoveList.append(move)
        result = getSolutionRecursive(currentBoard,localMoveList)
        if result != None:
            return result
    return None

def getAllBoardsInSolution(boardOrg, moveSequence):
    print("Total moves in solution: " + str(len(moveSequence)))
    print("Original board: ")
    printBoard(boardOrg)
    currentBoard = boardOrg
    boards = []
    for move in moveSequence:
        print("Making move: ")
        print(move)
        currentBoard = getNewBoardWithMove(currentBoard, move)
        boards.append(valueCopyBoard(currentBoard))
        printBoard(currentBoard)

    return boards

solution = getSolution()
getAllBoardsInSolution(startingBoard, solution)



