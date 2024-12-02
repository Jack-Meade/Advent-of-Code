#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read().split("\n")

def getPriority(item):
    ORD_UPPER, ORD_LOWER = 38, 96
    return ord(item) - (ORD_UPPER if item.isupper() else ORD_LOWER)

group = []
p1_total, p2_total = 0, 0
for rucksack in data:
    midpoint =  len(rucksack) // 2
    item     =  set(rucksack[:midpoint]).intersection(rucksack[midpoint:]).pop()
    p1_total += getPriority(item)
    
    group.append(rucksack)
    if len(group) == 3:
        group    =  [set(tmp) for tmp in group]
        item     =  group[0].intersection(group[1], group[2]).pop()
        p2_total += getPriority(item)
        group    =  []

print("Part1:", p1_total, "\nPart2:", p2_total)