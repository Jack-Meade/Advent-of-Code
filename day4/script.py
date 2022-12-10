#!/usr/bin/env python3

PART1 = True if 0 else False
FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read().split("\n")

def bad_pairing(e1, e2):
    e1_min, e1_max, e2_min, e2_max = int(e1[0]), int(e1[1]), int(e2[0]), int(e2[1])

    if PART1:
        if e1_min >= e2_min and e1_max <= e2_max: return True
        if e2_min >= e1_min and e2_max <= e1_max: return True
        return False
    else:
        e1, e2 = set([i for i in range(e1_min, e1_max + 1)]), set([i for i in range(e2_min, e2_max + 1)])
        return True if e1.intersection(e2) else False

total = 0
for pair in data:
    e1, e2 = pair.split(",")
    e1, e2 = e1.split("-"), e2.split("-")
    if bad_pairing(e1, e2): total += 1

print(f"Part {1 if PART1 else 2}: {total}")
