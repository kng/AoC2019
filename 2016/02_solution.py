# --- Day 2: Bathroom Security ---
# https://adventofcode.com/2016/day/2

import time
simple = False
verbose = 0

if simple:
    data = 'ULL\nRRDDD\nLURDL\nUUUUD'.splitlines()
else:
    file = open('02_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    if verbose > 0:
        print('data: {}'.format(data))

    # part 1
    keypad1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    maxx = maxy = 2
    x = y = 1
    for row in data:
        if verbose > 1:
            print('row {}'.format(row))
        for i in range(len(row)):
            if row[i] == 'U' and x > 0:
                x -= 1
            elif row[i] == 'D' and x < maxx:
                x += 1
            elif row[i] == 'L' and y > 0:
                y -= 1
            elif row[i] == 'R' and y < maxy:
                y += 1
        print('{}'.format(keypad1[x][y]), end='')
    print('')

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2
    keypad2 = [['x', 'x', '1', 'x', 'x'],
               ['x', '2', '3', '4', 'x'],
               ['5', '6', '7', '8', '9'],
               ['x', 'A', 'B', 'C', 'x'],
               ['x', 'x', 'D', 'x', 'x']]
    maxx = maxy = 4
    x = 2
    y = 0
    for row in data:
        if verbose > 1:
            print('row {}'.format(row))
        for i in range(len(row)):
            if row[i] == 'U' and x > 0:
                if keypad2[x-1][y] != 'x':
                    x -= 1
            elif row[i] == 'D' and x < maxx:
                if keypad2[x+1][y] != 'x':
                    x += 1
            elif row[i] == 'L' and y > 0:
                if keypad2[x][y-1] != 'x':
                    y -= 1
            elif row[i] == 'R' and y < maxy:
                if keypad2[x][y+1] != 'x':
                    y += 1
        print('{}'.format(keypad2[x][y]), end='')
    print('')

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
