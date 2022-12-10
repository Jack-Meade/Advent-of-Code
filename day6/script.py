#!/usr/bin/env python3

PART1 = True if 0 else False
FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read()

window = 4 if PART1 else 14
for i in range(len(data)):
    chars = i - window
    if chars < 0: continue
    
    if len(set(data[chars:i])) == window:
        print(i)
        break