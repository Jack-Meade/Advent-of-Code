#!/usr/bin/env python3

import numpy as np

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = np.array([[col for col in row] for row in file.read().split("\n")])

def tree_is_visible(ri, ci):
    height = data[ri][ci]
    if len([h for h in data[ri,:ci]     if h >= height]) == 0: return True # left
    if len([h for h in data[ri,ci + 1:] if h >= height]) == 0: return True # right
    if len([h for h in data[:ri,ci]     if h >= height]) == 0: return True # top
    if len([h for h in data[ri + 1:,ci] if h >= height]) == 0: return True # bottom
    return False

def tree_scenic_score(ri, ci):
    height = data[ri][ci]
    left   = [h for h in data[ri,:ci]]
    right  = [h for h in data[ri,ci + 1:]]
    top    = [h for h in data[:ri,ci]]
    bottom = [h for h in data[ri + 1:,ci]]
    left.reverse()
    top.reverse()

    scores = [0, 0, 0, 0]
    for i, direction in enumerate([left, right, top, bottom]):
        for other_tree_height in direction:
            scores[i] += 1
            if other_tree_height >= height: break
    return np.prod(scores)

TOTAL_ROWS, TOTAL_COLS = len(data), len(data[0])
LAST_ROW, LAST_COL     = TOTAL_ROWS - 1, TOTAL_COLS - 1

visible, best_score = 0, 0
for ri in range(TOTAL_ROWS):
    for ci in range(TOTAL_COLS):
        if ri == 0 or ri == LAST_ROW or ci == 0 or ci == LAST_COL or tree_is_visible(ri, ci):
            visible += 1
        tree_score = tree_scenic_score(ri, ci)
        best_score = best_score if best_score > tree_score else tree_score

print(f"Part1: {visible}\nPart2: {best_score}")