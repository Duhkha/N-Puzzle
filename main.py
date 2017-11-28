from gen import *
import re
import argparse


class Node:

    grid = []
    n = 0
    h = 0
    g = 0
    f = 0
    visited = False


def read_puzzle(node, file):
    puzzle = []
    node.grid = []
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
    node.n = int(puzzle[0])
    puzzle.pop(0)
    puzzle = [x.strip().split(' ') for x in puzzle]
    for x in puzzle:
        for y in x:
            y = int(y)
            node.grid.append(y)
    node.grid = [node.grid[i:i + node.n] for i in range(0, len(node.grid), node.n)]


def main():
    parser = argparse.ArgumentParser(description='Choose the heuristic')
    parser.add_argument('-ham', action="store_true")
    parser.add_argument('-man', action="store_true")
    parser.add_argument('-linear', action="store_true")
    parser.add_argument('--file', '-f', type=str, required=False)
    parser.add_argument('--size', '-s', type=int, required=False)
    args = parser.parse_args()
    end = []
    if not args.ham and not args.man and not args.linear:
        parser.print_help()
        exit(1)
    if args.size is None and args.file is None:
        print("Either give a filename or a size to generate")
        exit(1)
    if args.size is not None and args.file is not None:
        print("Can't generate AND read from file...")
        exit(1)
    start = Node()
    if args.file is not None:
        read_puzzle(start, args.file)
    else:
        start.grid = gen(args.size)
    start.n = len(start.grid)
    end = make_goal(start.n)
    end = [end[i:i + start.n] for i in range(0, len(end), start.n)]


if __name__ == '__main__':
    main()
