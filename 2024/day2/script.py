#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
  data = file.read().split("\n")

def isLevelSafe(level):
  if level != sorted(level) and level != sorted(level, reverse=True):
    return False
  
  for i in range(len(level) - 1):
    diff = abs(level[i] - level[i + 1])
    if diff == 0 or diff > 3:
      return False
  
  return True

safe_levels = 0
for level in data:
  level = [int(i) for i in level.split(" ")]
  
  if (not isLevelSafe(level)):
    continue
  
  safe_levels += 1

print(safe_levels)