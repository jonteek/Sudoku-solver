'''
Author: Jonathan Ek
Last updated: 2017-11-12
Description: Sudoku solver
'''


squareContents = '200004000900007041600500200057600080000000000030008760001005008520800004000400002'
assert len(squareContents) == 81
rows = 'ABCDEFGHI'
columns = '123456789'

def crossLists(firstList,secondList):
    return [a+b for a in firstList for b in secondList]

def unitsContainingSquare(square,unitList): #Return the list of all units containing a specific square
    returnList = []
    copyOfUnitList = unitList[:]
    for j in copyOfUnitList:
        if square in j:
            copyOfList = j[:]
            copyOfList.remove(square)
            returnList.append(copyOfList)
    return returnList

def identifyImpossibleDigits(gameBoard,unitsOfSquare): #Identify which digits cannot be placed in a versatile square
    listToReturn = []
    for j in unitsOfSquare:
        for i in j:
            if (int(gameBoard[i]) > 0):
                listToReturn.append(gameBoard[i])
    return listToReturn

def updateImpossibleDigitsDictionary(gameBoard,unitsOfSquare):
    listToReturn = []
    for j in unitsOfSquare:
        for i in j:
            if(len(gameBoard[i]) == 1):
                listToReturn.append(gameBoard[i])
    return listToReturn

def identifyVersatileSquares(listOfSquares,gameBoard): #Identify which squares that has several options for a digit
    listToReturn = []
    for j in listOfSquares:
        if gameBoard[j] == '0':
            listToReturn.append(j)
    return listToReturn

def removeImpossibleDigitsFromBoard(gameBoard,impossibleDigitsDictionary):#Remove the possible candidates which cannot be placed in a square
    for j in sorted(impossibleDigitsDictionary):
        for i in impossibleDigitsDictionary[j]:
            if i in gameBoard[j]:
                gameBoard[j] = gameBoard[j].replace(i,"")
        
    return gameBoard
def updateVersatileSquares(gameBoard,versatileSquares):#Check if the versatile squares still are versatile and update them accordingly 
    for j in versatileSquares:
        if(len(gameBoard[j]) == 1):
            versatileSquares.remove(j)
    return versatileSquares


def solvePuzzle(gameBoard,listOfVersatileSquares,unitDictionary):
    for i in range(0,len(listOfVersatileSquares)):
        print(listOfVersatileSquares[i])
                        
lst = [1,2,3,4,5]

listOfUnits = [crossLists(row,columns) for row in rows] + [crossLists(rows,col) for col in columns] + [crossLists(a,b)
                                                                                                      for a in ['ABC','DEF','GHI']
                                                                                                       for b in ['123','456','789']]




listOfSquares = crossLists(rows,columns)
board = {listOfSquares[b]:squareContents[b] for b in range(0,len(squareContents))}
versatileSquares = identifyVersatileSquares(listOfSquares,board)
unitsDict = {square:unitsContainingSquare(square,listOfUnits) for square in sorted(listOfSquares)}
impossibleDigitsDictionary = {square:identifyImpossibleDigits(board,unitsDict[square]) for square in versatileSquares}
for j in sorted(board):
    if board[j] == '0':
        board[j] = '123456789'

        
board = removeImpossibleDigitsFromBoard(board,impossibleDigitsDictionary)
versatileSquares = updateVersatileSquares(board,versatileSquares)
impossibleDigitsDictionary = {square:updateImpossibleDigitsDictionary(board,unitsDict[square]) for square in versatileSquares}
board = removeImpossibleDigitsFromBoard(board,impossibleDigitsDictionary)
#for j in sorted(board):
 #   print(j,board[j])



