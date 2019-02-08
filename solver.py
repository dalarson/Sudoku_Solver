# David Larson
# 
# TO RUN:
# $ python3 solver.py puzzle1.txt
#
#

import sys

class Cell:

    def __init__(self, x, y, val, posMoves):
        self.x = x
        self.y = y
        self.val = val
        self.posMoves = posMoves

class Puzzle:

    def __init__(self, grid):
        newGrid = []
        for y, row in enumerate(grid):
            currRow = []
            for x, square in enumerate(row):
                currRow.append(Cell(x, y, square.val, []))
            newGrid.append(currRow)
        self.grid = newGrid

    def show(self):
        for line in self.grid:
            for digit in line:
                print("|" + str(digit.val), end = '')
            print("|")
        print()

    def isValid(self):
        return self.rowsValid() and self.columnsValid() and self.boxesValid()

    def rowsValid(self):
        for row in self.grid:
            if not checkArr([x.val for x in row]): 
                return False
        return True

    def columnsValid(self):
        for i in range(9):
            arr = [x[i] for x in self.grid]
            if not checkArr([x.val for x in arr]): 
                return False
        return True

    def boxesValid(self):
        boxes = [[[], [], []], [[], [], []], [[], [], []]]
        for y in range(9):
            for x in range(9):
                # print("grid[" + str(y) + "][" + str(x) + "] goes in box [" + str(int(y/3)) + "][" + str(int(x/3)) + "]")
                boxes[int(y/3)][int(x/3)].append(self.grid[y][x])
        for row in boxes:
            for arr in row:
                if not checkArr([x.val for x in arr]): 
                    return False
        return True


    def setSquare(self, x, y, val):
        self.grid[x][y] = Cell(x, y, val, [])

    def isFull(self):
        for row in self.grid:
            for digit in row:
                if digit.val == 0:
                    return False
        return True

def anydup(arr):
  seen = set()
  for x in arr:
    if x != 0 and x in seen: return True
    seen.add(x)
  return False

def checkArr(arr):
    for i in range(1, 10):
        return not anydup(arr)


def getFirstBlank(puz):
    for y, line in enumerate(puz.grid):
        for x, digit in enumerate(line):
            if digit.val == 0: return [digit.x, digit.y]

def solve(puz):
    full = puz.isFull()
    valid = puz.isValid()

    if not valid: 
        return 0
    else:
        if full:
            puz.show() 
            return 1

    blank = getFirstBlank(puz)
    newPuz = Puzzle(puz.grid)
    for i in range(1, 10):
        newPuz.setSquare(blank[1], blank[0], i)
        # print(blank)
        # newPuz.show()
        val = solve(newPuz)
        if val == 1: return 1
    # no possibilities worked for this cell, so return 0


def main():
    try:
        file = open(sys.argv[1], 'r').readlines()
    except IndexError:
        print("Invalid arguments. Command should be in the following format:\n$ python3 solver.py <input.txt>")
        quit()

    grid = []
    for y, line in enumerate(file):
        row = [int(x) for x in list(line.rstrip())]
        newRow = []
        for x, square in enumerate(row):
            newRow.append(Cell(x, y, square, []))
        grid.append(newRow)
    
    puz = Puzzle(grid)
    # puz.show()
    solve(puz)


main()