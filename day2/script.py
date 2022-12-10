#!/usr/bin/env python3

PART1 = False if 0 else True
FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read().split("\n")

SCORES = { "W": 6, "D": 3, "L": 0, "X": 1, "Y": 2, "Z": 3 }
RPS = { # 0:draw | 1:win | 2:loss
    "A": ("X", "Y", "Z"), # rock
    "B": ("Y", "Z", "X"), # paper
    "C": ("Z", "X", "Y")  # scissors
}

def part2(op, me):
    if "X" in me: return RPS[op][2]
    if "Y" in me: return RPS[op][0]
    if "Z" in me: return RPS[op][1]

total = 0
for round in data:
    op, me = round.split(" ")
    me = me if PART1 else part2(op, me)
    drawing, winning = RPS[op][0], RPS[op][1]

    if   me == drawing: result = "D"
    elif me == winning: result = "W"
    else:               result = "L"
    total += SCORES[me] + SCORES[result]

print(f"Part{1 if PART1 else 2}: {total}")