#!/usr/bin/env python3

PART1 = True if 0 else False
FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read()

window = 4 if PART1 else 14
for i in range(window, len(data)):
    if len(set(data[i - window:i])) == window:
        print(f"Part {1 if PART1 else 2}:", i)
        break