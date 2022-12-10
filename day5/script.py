#!/usr/bin/env python3

PART1 = True if 0 else False
FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    stacks_raw, commands = [], []
    for line in file:
        line = line.strip("\n")
        if "move" in line:
            commands.append(line.split(" "))
        elif line:
            stacks_raw.append(line + " ")

# parse stacks into lists
stacks = [[] for _ in stacks_raw.pop(-1).replace(" ", "")]
for line in stacks_raw:
    stack = 3
    for i in range(0, len(line), 4): # sliding window
        cur = line[i:i + 4]
        if "[" in cur:
            stacks[(stack // 3) - 1].append(cur.replace("[", "").replace("]", "").replace(" ", ""))
        stack += 3

# reverse for right order
for i in range(len(stacks)): 
    stacks[i].reverse()

# perform commands
for command in commands:
    num, stack_from, stack_to = int(command[1]), int(command[3]) - 1, int(command[5]) - 1
    crane = []
    for _ in range(num):
        crane.append(stacks[stack_from].pop())
    if not PART1: crane.reverse()
    stacks[stack_to] += crane

print(f"Part {1 if PART1 else 2}: ", end = "")
for stack in stacks:
    print(stack[-1], end = "")
print()
