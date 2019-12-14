import time
import copy
import math
simple = False
verbose = 0  # 0 = quiet, 1 = some info, 2 = babbling

if simple:
    # 5 * 5
    # data = ".#..#\n.....\n#####\n....#\n...##\n.....".splitlines()
    # data = "......#.#.\n#..#.#....\n..#######.\n.#.#.###..\n.#..#.....\n" \
    #       "..#....#.#\n#..#....#.\n.##.#..###\n##...#..#.\n.#....####".splitlines()
    data = ".#....#####...#..\n##...##.#####..##\n##...#...#.#####.\n..#.....X...###..\n..#.#.....#....##".splitlines()
else:
    file = open("10_input.txt", "r")
    data = file.read().splitlines()

width = len(data[0])
height = len(data)
asteroids = [[0] * width for i in range(height)]
astPos = []
origin = []
targets = []

def main():
    start_time = time.time()

    score = copy.deepcopy(asteroids)
    for y in range(height):
        for x in range(width):
            if data[y][x] == '#':
                asteroids[y][x] = 1
                astPos.append([y, x])
            if data[y][x] == 'X':
                asteroids[y][x] = 1
                astPos.append([y, x])
                origin.append([y, x])

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

    high = max([max(n) for n in score])
    print("highest score: %i" % high)
    for y in range(height):
        for x in range(width):
            if score[y][x] >= high and [y, x] not in origin:
                origin.append([y, x])

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    if len(origin) < 1:
        exit(0)
    print("origin found: " + str(origin[0]))

    target = 0
    while target < 200:
        temp = []
        ast = origin[0]
        ay, ax = ast
        field = copy.deepcopy(asteroids)
        field[ast[0]][ast[1]] = 0
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
                if verbose > 2:
                    print("shadows [%i, %i]" % (ny, nx))
                field[ny][nx] = 0
        if verbose > 1:
            print("last field after shadowing (%i)" % target)
        for y in range(height):
            for x in range(width):
                if field[y][x] == 1:
                    a = math.degrees(math.atan2(ay - y, ax - x) - math.pi/2)
                    if a < 0:
                        a += 360
                    temp.append([y, x, a])
                    asteroids[y][x] = 0
                    target += 1
        if len(temp) == 0:
            print("ran out")
            break
        temp.sort(key=sortbyangle)
        targets.append(temp)

    i = 199
    print("the 200'th asteroid: %i" % (targets[0][i][0] + targets[0][i][1] * 100))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


def sortbyangle(val):
    return val[2]


main()

