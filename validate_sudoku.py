"""
Given a Sudoku data structure with size NxN, N > 0 and √N == integer, write a method to validate if it has been
filled out correctly.

The data structure is a multi-dimensional Array, i.e:

[
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]
Rules for validation

Data structure dimension: NxN where N > 0 and √N == integer
Rows may only contain integers: 1..N (N included)
Columns may only contain integers: 1..N (N included)
'Little squares' (3x3 in example above) may also only contain integers: 1..N (N included)
"""


import math


class Sudoku:
    def __init__(self, field):
        self.field = field
        self.n = len(self.field)

    def is_valid(self):
        for row in self.field:
            if set(row) != set(range(1, self.n + 1)) or len(row) != self.n:
                return False
        for i in range(self.n):
            column = [self.field[j][i] for j in range(self.n)]
            if set(column) != set(range(1, self.n + 1)):
                return False
        little_square = []
        for a in range(0, self.n, int(math.sqrt(self.n))):
            for b in range(0, self.n, int(math.sqrt(self.n))):
                for i in range(int(math.sqrt(self.n))):
                    for j in range(int(math.sqrt(self.n))):
                        value = self.field[i + b][j + a] if type(self.field[i + b][j + a]) == int else 0
                        little_square.append(value)
                if set(little_square) != set(range(1, self.n + 1)):
                    return False
                little_square.clear()
        return True
