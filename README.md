Sudoku Solver

Written February 6, 2019 by David Larson

Program can be run using the following:

$ python solver.py <puzzle.txt>

where puzzle.txt is replaced with a file containing a sudoku puzzle to be solved. The file must
be formatted as follows:

000100203
402000070
501300400
...

Blank squares are represented as zeros.

To be added:

Currently, this program only runs a recursive backtracking algorithm on the game board. While this
algorithm will eventually find a solution if there is one, it is far from ideal. In the future I would
like to add a feature that populates a list of possible moves for each square on the board, and populate
the squares in the recursive function in that order. In this manner, we are essentially limiting the
number of branches at the top of the tree of possible solutions, hopefully decreasing overall run time.
This idea still needs more testing. Also I would like to implement code which populates those squares to
which other rules can be applied. For example, if there is only one possible value for a square, we ought
to put that value into it immediately. Then this square can be removed from the tree altogether.


