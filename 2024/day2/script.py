#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
  data = file.read().split("\n")

def get_order(level):
  if level[0] - level[1] < 0:
    return True
  elif level[0] - level[1] > 0:
    return False
  return None

def is_level_safe(level):
  ascending = get_order(level)
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

    abs_diff = abs(diff)
    if abs_diff == 0 or abs_diff > 3:
      return False
  
  return True

safe_levels = 0
for level in data:
  level = [int(i) for i in level.split(" ")]
  
  if (not is_level_safe(level)):
    continue
  
  safe_levels += 1

print(safe_levels)