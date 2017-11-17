puzzle = []
with open("puzzles/puzzle.txt") as f:
    for line in f:
        line = line.partition('#')[0]
        line = line.rstrip()
        line.split(" ")
        puzzle.append(line)
n = puzzle[0]
puzzle.pop(0)
puzzle = [x.strip().split(' ') for x in puzzle]
test = []
print(puzzle)
for x in puzzle:
    test.append(map(int, x))
