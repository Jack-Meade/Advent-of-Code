#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
  data = file.read().split("\n")

left = sorted([i.split(" ")[0] for i in data])
right = sorted([i.split(" ")[-1] for i in data])

print(sum([abs(int(left[i]) - int(right[i])) for i in range(len(left))]))

# Part 2

similarity = 0
for i in left:
  same = 0
  for j in right:
    if i == j:
      same += 1
  similarity += int(i) * same

print(similarity)