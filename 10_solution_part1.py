import time
import copy
import math
simple = False
verbose = 0  # 0 = quiet, 1 = some info, 2 = babbling

if simple:
    # data = ".#..#\n.....\n#####\n....#\n...##\n.....".splitlines()
    data = "......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n" \
           "..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####".splitlines()
else:
    file = open("10_input.txt", "r")
    data = file.read().splitlines()

width = len(data[0])
height = len(data)
asteroids = [[0] * width for i in range(height)]
astPos = []


def main():
    start_time = time.time()

    score = copy.deepcopy(asteroids)
    for y in range(height):
        for x in range(width):
            if data[y][x] == '#':
                asteroids[y][x] = 1
                astPos.append([y, x])

    if simple:
        print("asteroid field")
        print(astPos)
        for line in asteroids:
            print(line)

    for ast in astPos:
        ay, ax = ast
        field = copy.deepcopy(asteroids)
        field[ast[0]][ast[1]] = -1
        for pos in astPos:
            if ast == pos:
                continue
            y = pos[0]
            x = pos[1]
            dy = y - ay
            dx = x - ax
            gcd = math.gcd(abs(dx), abs(dy))
            dy //= gcd
            dx //= gcd
            for i in range(1, width+height):
                ny = y + dy * i
                nx = x + dx * i
                if ny > height - 1 or ny < 0 or nx > width - 1 or nx < 0:
                    break
                if verbose > 1:
                    print("shadows [%i, %i]" % (ny, nx))
                field[ny][nx] = 2
        score[ay][ax] = sum([n.count(1) for n in field])

    if simple:
        print("last field after shadowing")
        for line in field:
            print(line)

    if verbose > 0:
        print("scoreboard: ")
        for line in score:
            print(line)

    print("highest score: %i" % max([max(n) for n in score]))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - start_time))


main()

