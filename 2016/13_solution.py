# --- Day 13: A Maze of Twisty Little Cubicles ---
# https://adventofcode.com/2016/day/13

import time
simple = False
verbose = 0

if simple:
    data = 10
    size = 10
else:
    file = open('13_input.txt', 'r')
    data = int(file.read().strip())
    size = 50


def main():
    start_time = time.time()
    if verbose > 0:
        print('puzzle input {}'.format(data))

    # part 1 and 2 combined
    maze = []
    for y in range(size):  # generate maze
        row = []
        for x in range(size):
            i = x*x + 3*x + 2*x*y + y + y*y + data
            d = len(str(bin(i))[2:].replace('0', '')) % 2
            if d == 1:
                row += '#'
            else:
                row += '.'
        maze += [row]

    startx = starty = 1
    if simple:
        stopx = 7
        stopy = 4
    else:
        stopx = 31
        stopy = 39

    s = [[0, starty, startx]]
    maze[starty][startx] = 0
    maxstep = 50
    loc = 0
    while s:
        i, y, x = s.pop(0)
        if y == stopy and x == stopx:
            print('part 1, found shortest path: {}'.format(i))
            break
        if i <= maxstep:
            loc += 1

        if x - 1 >= 0 and maze[y][x - 1] == '.':
            maze[y][x - 1] = str(i)
            s.append([i + 1, y, x - 1])

        if x + 1 < size and maze[y][x + 1] == '.':
            maze[y][x + 1] = str(i)
            s.append([i + 1, y, x + 1])

        if y - 1 >= 0 and maze[y - 1][x] == '.':
            maze[y - 1][x] = str(i)
            s.append([i + 1, y - 1, x])

        if y + 1 < size and maze[y + 1][x] == '.':
            maze[y + 1][x] = str(i)
            s.append([i + 1, y + 1, x])

        if verbose > 1:
            print('i: {}, x: {}, y: {}'.format(i, x, y))

    if verbose > 1:
        for row in maze:
            print(row)
    print('part 2, distinct locations in {} steps: {}'.format(maxstep, loc))

    end_time = time.time()
    print("time elapsed: {} seconds".format(end_time - start_time))


if __name__ == '__main__':
    main()
