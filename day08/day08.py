# https://adventofcode.com/2022/day/8
from Grid2D import Grid2D

with open('input.txt', 'r') as file:
    raw_input = file.read()
    lines = raw_input.splitlines()

# --- Part 1 --- #

grid = Grid2D(lines)


class Trees:

    def __init__(self, grid: Grid2D):
        self.grid = grid

    def is_visible(self, tree_x, tree_y):
        x_range, y_range = self.grid.dimensions()
        tree = self.grid.get(tree_x, tree_y)
        if tree_x in x_range or tree_y in y_range:
            return True

        visible = self.north(tree_x, tree_y, tree)[0] or self.south(tree_x, tree_y, tree)[0] or \
                  self.east(tree_x, tree_y,
                            tree)[0] or self.west(
            tree_x, tree_y, tree)[0]
        return visible

    def scenic_score(self, tree_x, tree_y):
        tree = self.grid.get(tree_x, tree_y)
        scenic_score = self.north(tree_x, tree_y, tree)[1] * self.south(tree_x, tree_y, tree)[1] * \
                       self.east(tree_x, tree_y, tree)[1] * self.west(
            tree_x, tree_y, tree)[1]
        return scenic_score

    def all_scenic_scores(self):
        x_range, y_range = self.grid.dimensions()
        x_min, x_max = x_range
        y_min, y_max = y_range

        all_scores = []
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                all_scores.append(self.scenic_score(x, y))
        return all_scores

    def count_visible(self):
        count = 0
        x_range, y_range = self.grid.dimensions()
        x_min, x_max = x_range
        y_min, y_max = y_range
        for y in range(y_min, y_max + 1):
            for x in range(x_min, x_max + 1):
                if self.is_visible(x, y):
                    count += 1
        return count

    def south(self, tree_x, tree_y, tree):
        _, y_range = self.grid.dimensions()
        y_min, y_max = y_range

        count = 0
        for y in range(tree_y + 1, y_max + 1):
            count += 1
            if self.grid.get(tree_x, y) >= tree:
                return False, count
        return True, count

    def north(self, tree_x, tree_y, tree):
        _, y_range = self.grid.dimensions()
        y_min, y_max = y_range

        count = 0
        for y in range(tree_y - 1, y_min - 1, -1):
            count += 1
            if self.grid.get(tree_x, y) >= tree:
                return False, count
        return True, count

    def east(self, tree_x, tree_y, tree):
        x_range, _ = self.grid.dimensions()
        x_min, x_max = x_range

        count = 0
        for x in range(tree_x + 1, x_max + 1):
            count += 1
            if self.grid.get(x, tree_y) >= tree:
                return False, count
        return True, count

    def west(self, tree_x, tree_y, tree):
        x_range, _ = self.grid.dimensions()
        x_min, x_max = x_range

        count = 0
        for x in range(tree_x - 1, x_min - 1, -1):
            count += 1
            if self.grid.get(x, tree_y) >= tree:
                return False, count
        return True, count


trees = Trees(grid)
print(trees.count_visible())

# --- Part 2 --- #
print(max(trees.all_scenic_scores()))
