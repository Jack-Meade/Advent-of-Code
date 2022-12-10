#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read().split("\n\n")

calories = [sum([int(item_cal) for item_cal in elf_inv.split("\n") if item_cal]) for elf_inv in data]
print("Part 1:", max(calories))

top3 = 0
for i in range(3):
    top = max(calories)
    top3 += top
    calories.pop(calories.index(top))
print("Part 2:", top3)