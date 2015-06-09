import profile
from pprint import pprint

def sudoku(puzzle):
    def solve(puzzle):
        r = get_best_next_empty(puzzle)
        if not r:
            return puzzle
        else:
            candidates = get_candidates(puzzle, *r)
            for c in candidates:
                    puzzle[r[0]][r[1]] = c
                    if solve(puzzle):
                        return puzzle
                    puzzle[r[0]][r[1]] = 0

        return False
    obj_puzzle = puzzle
    return solve(obj_puzzle)

def is_pos_valid(puzzle, i, j, n):
    if n in puzzle[i]:
        return False
    for k in range(0, 9):
        if n == puzzle[k][j]:
            return False
    bi = i / 3
    bj = j / 3
    for sqi in range(0, 3):
        for sqj in range(0, 3):
            if n == puzzle[sqi + 3 * bi][sqj + 3 * bj]:
                return False
    return True

def get_best_next_empty(puzzle):
    def count_options(x, y):
        c = 0
        for i in range(0, 9):
            if is_pos_valid(puzzle, x, y, i):
                c += 1
        return c
    min_count = 10
    min_pos = None
    for i in range(0, 9):
        for j in range(0, 9):
            if puzzle[i][j] == 0:
                c = count_options(i, j)
                if  c < min_count:
                    min_count = c
                    min_pos = (i, j)
    return min_pos

def get_candidates(puzzle,x, y):
    res = []
    for i in range(1, 10):
        if is_pos_valid(puzzle, x, y, i):
            res.append(i)
    return res

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

puzzle2 = [[0, 0, 6, 0, 2, 0, 0, 5, 0],
           [0, 0, 2, 0, 0, 0, 1, 9, 4],
           [0, 0, 0, 1, 0, 0, 2, 0, 7],
            [6, 0, 7, 0, 8, 2, 0, 1, 9],
            [0, 8, 5, 0, 7, 0, 0, 3, 0],
             [0, 0, 0, 6, 0, 5, 4, 0, 0],
             [0, 9, 0, 0, 1, 3, 0, 4, 0],
             [0, 0, 1, 0, 0, 9, 0, 0, 0],
             [7, 3, 0, 0, 0, 8, 9, 0, 0]]
#profile.run('print sudoku(puzzle); print')
pprint(sudoku(puzzle2))

