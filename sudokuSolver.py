'''
    Solves 9x9 sudoku puzzles.
    Copyright (C) 2014 Philip Hodder

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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
'''
TODO:
Change checklist check if possible, else make a function to check.
'''
def checkRows():
    global board 
    for row in board:
        checklist = [False]*9
        for num in row:
            if (num-1 == -1):
                continue
            if (checklist[num-1]):
                return False
            checklist[num-1] = True
    return True

'''
TODO:
Change checklist check if possible, else make a function to check.
'''    
def checkCols():
    global board
    for i in range(0,9):
        checklist = [False]*9
        for row in board:
            if (row[i]-1 == -1):
                continue
            if (checklist[row[i]-1]):
                return False
            checklist[row[i]-1] = True
    return True

'''
Checks all 3x3 boxes in the sudoku puzzle
'''
def checkBoxes():
    global board
    boxSize = 3
    for i in range(0,boxSize):
        for j in range(0, boxSize):
            if (not checkBox(i*boxSize,j*boxSize)):
                return False
    return True

'''
Checks a 3x3 space around the starting space
'''
def checkBox(x,y):
    global board
    boxSize = 3
    checklist = [False]*9
    for row in range(y, y+boxSize):
        for col in range(x, x+boxSize):
            if (board[row][col]-1 == -1):
                continue
            if (checklist[board[row][col]-1]):
                return False
            checklist[board[row][col]-1] = True
    return True
    
def checkSolve():
    return checkRows() and checkCols() and checkBoxes()
    
def solve():
    print "I will be smart and finish a Sudoku one day!"
    
printBoard()
print checkSolve()
