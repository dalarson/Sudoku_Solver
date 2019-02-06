# David Larson
# 
# TO RUN:
# $ python3 solver.py puzzle1.txt
#
#

import sys

class Puzzle:

    def __init__(self, grid):
        self.grid = grid

    def show(self):
        for line in self.grid:
            for digit in line:
                print("|" + str(digit), end = '')
            print("|")
        print()

    def isValid(self):
        return self.rowsValid() and self.columnsValid() and self.boxesValid()

    def rowsValid(self):
        return True

    def columnsValid(self):
        return True

    def boxesValid(self):
        return True

    def setSquare(self, x, y, val):
        self.grid[x][y] = val

    def isFull(self):
        for row in self.grid:
            for digit in row:
                if digit == 0:
                    return False
        return True


def getFirstBlank(puz):
    for y, line in enumerate(puz.grid):
        for x, digit in enumerate(line):
            if digit == 0:
                return [x, y]

def solve(puz):
    if puz.isFull():
        puz.show()
        return 1
    blank = getFirstBlank(puz)

    newPuz = Puzzle(puz.grid)
    for i in range(1, 10):
        newPuz.setSquare(blank[1], blank[0], i)
        if solve(newPuz) == 1: return 1


def main():
    try:
        file = open(sys.argv[1], 'r').readlines()
    except IndexError:
        print("Invalid arguments. Command should be in the following format:\n$ python3 solver.py <input.txt>") 

    grid = []
    for line in file:
        grid.append([int(x) for x in list(line.rstrip())])
    
    puz = Puzzle(grid)
    puz.show()
    solve(puz)


main()