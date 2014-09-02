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
Change checklist initialisation, into short hand (currently forgotten
and no internet source).
Change checklist check if possible, else make a function to check.
'''
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

'''
TODO:
Change checklist initialisation, into short hand (currently forgotten
and no internet source).
Change checklist check if possible, else make a function to check.
'''    
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

'''
TODO:
Finish implementing, will need some thinking to organise elegantly
'''
def checkBoxes():
    global board
    box = 3
    for x in range(0, box):
        for y in range(0, box):
            for i in range(0,box):
                for j in range(0, box):
                    print board[y*box + i][x*box + j],
                print
            print "------"
        print "*****"
    return True
        
def checkSolve():
    return checkRows() and checkCols() and checkBoxes()
    
def solve():
    print "I will be smart and finish a Sudoku one day!"
    
printBoard()
print checkSolve()
