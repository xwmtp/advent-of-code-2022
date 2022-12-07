# https://adventofcode.com/2022/day/7

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()


# --- Part 1 --- #

class Dir:

    def __init__(self, name: str, parent):
        self.name = name
        self.children = dict()
        self.parent = parent

    def get_child_dir(self, name):
        if name not in self.children:
            self.children[name] = Dir(name, self)
        return self.children[name]

    def get_child_file(self, name, size):
        if name not in self.children:
            self.children[name] = File(name, size)
        return self.children[name]

    def to_string(self, depth=1):
        lines = [' ' * depth + f'- {self.name} (dir)']
        for line in [' ' * depth + s.to_string(depth + 1) for s in self.children.values()]:
            lines.append(line)
        return '\n'.join(lines)

    def is_leaf_dir(self):
        return len([child for child in self.children.values() if type(child) is Dir]) == 0

    def get_size(self):
        return sum(child.get_size() for child in self.children.values())

    def get_all_dir_sizes(self):
        if self.is_leaf_dir():
            return self.get_size()
        children_sizes = [self.get_size()] + [child.get_all_dir_sizes() for child in self.children.values() if
                                              type(child) is Dir]
        return flatten(children_sizes)


class File:

    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def to_string(self, depth=1):
        return ' ' * depth + f'- {self.name} (file, size={self.size})'

    def get_size(self):
        return self.size

    def get_all_children_sizes(self):
        return self.name, self.get_size()


tree = Dir('/', None)
wd = tree

for line in lines:
    if line.startswith('$ cd /'):
        wd = tree
    elif line.startswith('$ cd ..'):
        if wd.parent is None:
            raise Exception(f'Cannot cd .. to parent of {wd.name}')
        wd = wd.parent
    elif line.startswith('$ cd'):
        arg = line[5:]
        wd = wd.get_child_dir(arg)
    elif line.startswith('dir '):
        arg = line[4:]
        wd.get_child_dir(arg)
    elif line.startswith('$ ls'):
        continue
    else:
        size_string, file_name = line.split(' ')
        wd.get_child_file(file_name, int(size_string))


def flatten(lst):
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])


dir_sizes = tree.get_all_dir_sizes()
print(sum(dir_size for dir_size in dir_sizes if dir_size <= 100000))

# --- Part 1 --- #
disk_space = 70000000
needed_for_update = 30000000
remaining = disk_space - tree.get_size()
need_to_free_up = needed_for_update - remaining

big_enough = [c for c in flatten(tree.get_all_dir_sizes()) if c >= need_to_free_up]
print(min(big_enough))
