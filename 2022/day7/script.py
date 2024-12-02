#!/usr/bin/env python3

FILENAME = "example.txt" if 0 else "input.txt"
with open(FILENAME, "r") as file:
    data = file.read().split("\n")[1:]

MAX_SIZE    = 100_000
TOTAL_DISK  = 70_000_000
UNUSED_DISK = 30_000_000
current_dir = "root"
tree        = {current_dir: {"size": 0, "children": []}}

for line in data:
    if line.startswith("$"):
        if "cd" in line:
            if ".." in line:
                current_dir = "/".join(current_dir.split("/")[:-1])
            else:
                _, _, dirname = line.split(" ")
                current_dir = current_dir + "/" + dirname  
                tree[current_dir] = {"size": 0, "children": []}
    else:
        size, name = line.strip("\n").split(" ")
        name = name if "dir" not in size else current_dir + "/" + name
        tree[current_dir]["children"].append((size, name))

# sort depth ascending to not double count
for dir in [dir for dir in sorted(tree.keys(), key=lambda key: key.count("/"), reverse=True)]:
    dir_size = 0
    for file_size, name in tree[dir]["children"]:
        dir_size += tree[name]["size"] if "dir" == file_size else int(file_size)
    tree[dir]["size"] = dir_size

dirs_to_del = list(filter(lambda dir: dir[1]["size"] < MAX_SIZE, tree.items()))
print("Part1:", sum([dir[1]["size"] for dir in dirs_to_del]))

space_needed = UNUSED_DISK - (TOTAL_DISK - tree["root"]["size"])
# sort sizes descending and find first dir with needed size
for dir in [dir for dir in sorted(tree.keys(), key=lambda key: tree[key]["size"])]:
    if tree[dir]["size"] >= space_needed:
        print("Part2:", tree[dir]["size"])
        break