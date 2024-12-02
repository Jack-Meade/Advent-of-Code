#!/usr/bin/env python3

FILENAME = "example.txt"# if 0 else "input.txt"
with open(FILENAME, "r") as file:
    commands = file.read().split("\n")

DIRECTION_LOOKUP = {
    "U": (True,  1,  0),
    "D": (True, -1,  0),
    "R": (False, 0,  1),
    "L": (False, 0, -1)
}

tail = {"x": 0, "y": 0, "previous": {"00": None}}
previous = DIRECTION_LOOKUP[commands[0].split(" ")[0]][0]
for command in commands:
    direction, steps       = command.split(" ")
    isVertical, ymod, xmod = DIRECTION_LOOKUP[direction]

    # do corrective step when changing directions from x/y axes
    if previous != isVertical:
        pass
    for step in range(int(steps)):
        tail["y"] += ymod
        tail["x"] += xmod
        current_pos = f"{tail['y']}{tail['x']}"
        if current_pos not in tail["previous"]:
            tail["previous"][current_pos] = True
        print(current_pos)
    previous = isVertical

print("Part1:", len(tail["previous"].keys()))