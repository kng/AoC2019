# --- Day 1: No Time for a Taxicab ---
# https://adventofcode.com/2016/day/1

import time
simple = False
verbose = 1

if simple:
    # data = 'R5, L5, R5, R3'.split(', ')
    data = 'R8, R4, R4, R8'.split(', ')
else:
    file = open('01_input.txt', 'r')
    data = file.read().strip().split(', ')


class Ship(object):
    def __init__(self, d=0, x=0, y=0):
        self.dir = d  # 0=N, 1=E, 2=S, 3=W
        self.dirAsc = ['north', 'east', 'south', 'west']
        self.x = x  # +N / -S
        self.y = y  # +E / -W
        self.validCmd = ['R', 'L']
        self.track = []
        self.destination = []

    def reset(self, d=0, x=0, y=0):
        self.dir = d
        self.x = x
        self.y = y

    def command(self, cmd):
        if len(cmd) > 1:
            if cmd[0] in self.validCmd:
                dist = int(cmd[1:])
                if cmd[0] == 'R':
                    self.dir += 1
                    self.dir %= 4
                elif cmd[0] == 'L':
                    self.dir -= 1
                    self.dir %= 4
                for i in range(dist):
                    if self.dir == 0:
                        self.x += 1
                    elif self.dir == 1:
                        self.y += 1
                    elif self.dir == 2:
                        self.x -= 1
                    else:
                        self.y -= 1
                    if (self.x, self.y) in self.track and self.destination == []:
                        self.destination = (self.x, self.y)
                    self.track.append((self.x, self.y))
            else:
                print('invalid command')
        else:
            print('command too short')

    def print(self):
        print('Ship position: {} units {}, {} units {}, facing {}'
              .format(abs(self.y), self.dirAsc[1] if self.y >= 0 else self.dirAsc[3],
                      abs(self.x), self.dirAsc[0] if self.x >= 0 else self.dirAsc[2],
                      self.dirAsc[self.dir]))


def main():
    start_time = time.time()

    ship = Ship()
    for row in data:
        ship.command(row)
        if verbose > 1:
            print('{} '.format(row), end='')
            ship.print()
    print('distance: {}'.format(abs(ship.x) + abs(ship.y)))
    # part 2
    print('destination: {}'.format(abs(ship.destination[0]) + abs(ship.destination[1])))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
