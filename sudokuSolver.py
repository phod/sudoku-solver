board = [[1,2,3,4,5,6,7,8,9],
         [4,5,6,7,8,9,1,2,3],
         [7,8,9,1,2,3,4,5,6],
         [2,3,4,5,6,7,8,9,1],
         [5,6,7,8,9,1,2,3,4],
         [8,9,1,2,3,4,5,6,7],
         [3,4,5,6,7,8,9,1,2],
         [6,7,8,9,1,2,3,4,5],
         [9,1,2,3,4,5,6,7,8]]

def printBoard():
    global board
    for row in board:
        for cell in row:
            print cell,
        print

def checkRows():
    global board
    
    for row in board:
        checklist = [False, False, False, False, False, False, False, False, False]
        for num in row:
            checklist[num-1] = True
        
        for num in checklist:
            if not num:
                return False
    return True
    
def checkCols():
    global board
    for i in range(0,9):
        checklist = [False, False, False, False, False, False, False, False, False]
        for row in board:
            checklist[row[i]-1] = True
        for num in checklist:
            if not num:
                return False
        return True

def checkBoxes():
    global baord
    box = 3
    for mult in range(1,4):
        print mult

def checkSolve():
    return checkRows() and checkCols() and checkBoxes()
    
    
printBoard()
print checkRows()
print checkCols()
print checkBoxes()
