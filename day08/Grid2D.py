class Grid2D:

    def __init__(self, rows):
        self.grid = rows

    def size(self):
        if len(self.grid) > 0:
            return len(self.grid[0]), len(self.grid)
        else:
            return 0, 0

    def get(self, x, y):
        return self.grid[y][x]

    def set(self, x, y, to):
        self.grid[y][x] = to

    def dimensions(self):
        return (0, len(self.grid[0]) - 1), (0, len(self.grid) - 1)

    def __str__(self):
        return '\n'.join([''.join(str(r) for r in row) for row in self.grid])

    def copy(self):
        return Grid2D([row.copy() for row in self.grid])
