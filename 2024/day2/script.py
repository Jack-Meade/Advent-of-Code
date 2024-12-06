#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
  data = file.read().split("\n")

def is_ascending(level):
  if level[0] - level[1] < 0:
    return True
  elif level[0] - level[1] > 0:
    return False
  return None

def is_level_safe(level):
  ascending = is_ascending(level)
  if ascending == None:
    return False
  
  for i in range(len(level) - 1):
    diff = level[i] - level[i + 1]
    if diff == 0:
      return False
    if diff < 0 and not ascending:
      return False
    if diff > 0 and ascending:
      return False
    if abs(diff) > 3:
      return False
  
  return True

safe_levels = 0
for level in data:
  working_level = level = [int(i) for i in level.split(" ")]
  
  current = 0
  while not is_level_safe(working_level):
    if current == len(level):
      break
    working_level = list(level)
    working_level.pop(current)
    current += 1
  
  if not current == len(level):
    safe_levels += 1

print(safe_levels)