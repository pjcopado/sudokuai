import numpy as np
from sudokuai import utils

test = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [4, 5, 6, 7, 8, 9, 1, 2, 3],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [2, 3, 4, 5, 6, 7, 8, 9, 1],
    [5, 6, 7, 8, 9, 1, 2, 3, 4],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [3, 4, 5, 6, 7, 8, 9, 1, 2],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
    ])

board_zeroes = np.zeros(shape=(9,9), dtype=int)
board_zeroes[0,0] = 7
board_zeroes[8,0] = 1


WIN_SET = {n for n in range(1, 10)}

def next_empty(grid):
    for x, row in enumerate(grid):
        for y, col in enumerate(row):
            if col == 0:
                return (x, y)
    return (None, None)

def is_valid(grid, x, y, value):
    not_in_row =  value not in grid[x]
    not_in_col =  value not in grid[:, y]
    X = (x // 3) * 3
    Y = (y // 3) * 3
    not_in_box =  value not in grid[X:X+3, Y:Y+3]
    return not_in_row and not_in_col and not_in_box

def fill_empty(grid, x, y):
    for value in WIN_SET:
        if is_valid(grid, x, y, value):
            grid[x, y] = value
            break

def check_solution(grid):
    row_ok = all([set(x) == WIN_SET for x in grid])
    col_ok = all([set(y) == WIN_SET for y in grid.T])
    #box_ok = [set(box) == WIN_SET for box in [grid[X:X+3, X:X+3] for X in [0, 3, 6]]]
    box_ok = True #TODO
    return row_ok and col_ok and box_ok

def solve(grid):
    #grid = np.copy(grid)
    x, y = next_empty(grid)
    if x is None:
        return True
    for value in WIN_SET:
        if is_valid(grid, x, y, value):
            grid[x, y] = value
            if solve(grid):
                return True
            grid[x, y] = 0
    return False
