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
import fileinput

board = [[1,2,3,4,5,6,7,8,9],
         [4,5,6,7,8,9,1,2,3],
         [7,8,9,1,2,3,4,5,6],
         [2,3,4,5,6,7,8,9,1],
         [5,6,7,8,9,1,2,3,4],
         [8,9,1,2,3,4,5,6,7],
         [3,4,5,6,7,8,9,1,2],
         [6,7,8,9,1,2,3,4,5],
         [9,1,2,3,4,5,6,7,8]]

'''
Print the board row by row
'''
def printBoard():
    global board
    for row in board:
        for cell in row:
            print cell,
        print
'''
Checks to see if any numbers are double up in each row
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
Checks to see if any numbers are doubled up in each col
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

'''
Algorithm to implement.
Find the next empty position
insert a number between 1 and 9
if legal call solve
if solved, break
'''
def solve():
    global board
    pos = findEmpty()
    row = pos[0]
    col = pos[1]
    solved = False
    if (col == -1 and row == -1):
        return True
    for i in range (1, 10):
        board[row][col]=i
        if checkSolve():
            solved = solve()
        if (solved):
            return True
    board[row][col]=0                
    return False
            
def findEmpty():
    global board
    for row in range(0,9):
        for col in range(0,9):
            if (board[row][col]==0):
                val = [row,col]
                return val
    return [-1,-1]
    
def isNum(c):
    return c>='0' and c<='9'
    
def readInput():
    global board
    row = 0
    col = 0
    for line in fileinput.input():
        for ch in line:
            if (isNum(ch)):
                board[row][col]=int(ch)
                col += 1
                if(col==9):
                    col = 0
                    row += 1

def main():
    readInput()
    if (solve()):
        print "The solution to the sudoku is:"
        printBoard()
    else:
        print "There is no solution to the sudoku:"
        printBoard()
        
main()
