#!/usr/bin/env python

import re
import argparse


class Node:
    i = 0
    h = 0
    n = 0
    x0 = 0
    y0 = 0
    up_h = 0
    down_h = 0
    left_h = 0
    right_h = 0
    heuristic = 0
    grid = []
    end = []

    def hamming(self):
        i = 0
        h = 0
        while i < self.n:
            j = 0
            while j < self.n:
                if self.grid[i][j] != 0 and self.end[i][j] != self.grid[i][j]:
                    h += 1
                j += 1
            i += 1
        print(h)
        return h
        # number of tiles out of place

    def manhattan_distance(self):
        print(self.grid)
        return 0
        # number of moves required to get to

    def linear_conflict(self):
        print(self.grid)
        return 0
        # Manhattan distance + 2*number of linear conflicts

    def up(self):
        tmp = self.grid
        tmp[self.x0][self.y0] = tmp[self.x0 + 1][self.y0]
        tmp[self.x0 + 1][self.y0] = 0
        if self.heuristic == 0:
            self.up_h = self.hamming()
        elif self.heuristic == 1:
            self.up_h = self.manhattan_distance()
        else:
            self.up_h = self.linear_conflict()

    def down(self):
        tmp = self.grid
        tmp[self.x0][self.y0] = tmp[self.x0 - 1][self.y0]
        tmp[self.x0 - 1][self.y0] = 0
        if self.heuristic == 0:
            self.down_h = self.hamming()
        elif self.heuristic == 1:
            self.down_h = self.manhattan_distance()
        else:
            self.down_h = self.linear_conflict()

    def left(self):
        tmp = self.grid
        tmp[self.x0][self.y0] = tmp[self.x0][self.y0 - 1]
        tmp[self.x0][self.y0 - 1] = 0
        if self.heuristic == 0:
            self.down_h = self.hamming()
        elif self.heuristic == 1:
            self.down_h = self.manhattan_distance()
        else:
            self.down_h = self.linear_conflict()

    def right(self):
        tmp = self.grid
        tmp[self.x0][self.y0] = tmp[self.x0][self.y0 + 1]
        tmp[self.x0][self.y0 + 1] = 0
        if self.heuristic == 0:
            self.down_h = self.hamming()
        elif self.heuristic == 1:
            self.down_h = self.manhattan_distance()
        else:
            self.down_h = self.linear_conflict()

    def check_moves(self):
        self.x0 = 0
        found = False
        while self.x0 < self.n and not found:
            self.y0 = 0
            while self.y0 < self.n:
                if self.grid[self.x0][self.y0] == 0:
                    found = True
                    break
                self.y0 += 1
            if found:
                break
            self.x0 += 1
        if self.x0 < self.n:
            self.up()
        else:
            self.up_h = 9999
        if self.x0 > 0:
            self.down()
        else:
            self.down_h = 9999
        if self.y0 > self.n:
            self.left()
        else:
            self.left_h = 9999
        if self.y0 > 0:
            self.down()
        else:
            self.down_h = 9999
        pass

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

    def read_end(self, file):
        puzzle = []
        self.end = []
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
            self.end.append(map(int, x))

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


def solve(node):
    node.check_moves()


parser = argparse.ArgumentParser(description='Choose the heuristic')
parser.add_argument('-ham', action="store_true")
parser.add_argument('-man', action="store_true")
parser.add_argument('-linear', action="store_true")
args = parser.parse_args()

if not args.ham and not args.man and not args.linear:
    parser.print_help()
    exit(1)

start = Node()
start.read_puzzle("puzzles/puzzle.txt")
start.read_end("puzzles/end.txt")
if not start.is_solvable():
    print("the puzzle is not solvable")
    exit(1)
else:
    print("this puzzle is solvable")

if args.ham:
    start.heuristic = 0
    solve(start)
elif args.man:
    start.heuristic = 1
elif args.linear:
    start.heuristic = 2






