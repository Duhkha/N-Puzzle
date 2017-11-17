class Node:
    i = 0
    h = 0
    n = 0
    grid = []

    def manhattan_distance(self):
        print(self.grid)
        # number of moves required to get to

    def linear_conflict(self):
        print(self.grid)
        # Manhattan distance + 2*number of linear conflicts

    def hamming(self):
        print(self.grid)
        # number of tiles out of place

    def read_puzzle(self, file):
        puzzle = []
        with open(file) as f:
            for line in f:
                line = line.partition('#')[0]
                line = line.rstrip()
                line.split(" ")
                puzzle.append(line)
        self.n = int(puzzle[0])
        puzzle.pop(0)
        puzzle = [x.strip().split(' ') for x in puzzle]
        for x in puzzle:
            self.grid.append(map(int, x))


start = Node()
end = Node()
start.read_puzzle("puzzles/puzzle.txt")
start.read_puzzle("puzzles/end.txt")
print(start.grid)

