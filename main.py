#!/usr/bin/env python

import re
import argparse

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
        self.grid = []
        with open(file) as f:
            for line in f:
                line = line.partition('#')[0]
                line = line.rstrip()
                line = line.lstrip()
                line = re.sub(' +', ' ', line)
                line.split(" ")
                puzzle.append(line)
        if puzzle[0] == '':
            puzzle.pop(0)
        self.n = int(puzzle[0])
        puzzle.pop(0)
        puzzle = [x.strip().split(' ') for x in puzzle]
        for x in puzzle:
            self.grid.append(map(int, x))

    def is_solvable(self):
        temp = []
        solvable = False
        for i in self.grid:
            for j in i:
                temp.append(j)
        inv_count = 0
        i = 0
        while i < self.n * self.n - 1:
            j = i + 1
            while j < self.n * self.n:
                if temp[i] != 0 and temp[j] != 0 and temp[i] > temp[j]:
                    inv_count += 1
                j += 1
            i += 1
        x_pos = 0
        i = self.n - 1
        while i >= 0:
            j = self.n - 1
            while j >= 0:
                if self.grid[i][j] == 0:
                    x_pos = self.n - i
                j -= 1
            i -= 1
        if self.n % 2 == 1:
            if inv_count % 2 == 0:
                solvable = True
        else:
            if x_pos % 2 == 0:
                if inv_count % 2 == 1:
                    solvable = True
            else:
                if inv_count % 2 == 0:
                    solvable = True
        return solvable


parser = argparse.ArgumentParser(description='Choose the heuristic')
parser.add_argument('-ham', action="store_true")
parser.add_argument('-man', action="store_true")
parser.add_argument('-linear', action="store_true")
args = parser.parse_args()


if args.ham:
    print("ham")
elif args.man:
    print("man")
elif args.linear:
    print("linear")
else:
    parser.print_help()
    exit(1)
start = Node()
end = Node()
start.read_puzzle("puzzles/puzzle.txt")
end.read_puzzle("puzzles/end.txt")
if not start.is_solvable():
    print("the puzzle is not solvable")
    exit(1)
else:
    print("this puzzle is solvable")
print(end.grid)
print(start.grid)

