import numpy as np
import time
simple = False
# simple = True
start_time = time.time()

if simple:
    # file = open("03_simple.txt", "r")
    # data = file.read().splitlines()

    # distance 6
    # data = "R8,U5,L5,D3\nU7,R6,D4,L4".splitlines()
    # distance 159
    # data = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83".splitlines()
    # distance 135
    # data = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7"

    # part two
    # data = "R75,D30,R83,U83,L12,D49,R71,U7,L72\nU62,R66,U55,R34,D71,R55,D58,R83".splitlines()  # 610 steps
    data = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51\nU98,R91,D20,R16,D67,R40,U7,R15,U6,R7".splitlines()  # 410 steps
    fieldWidth = 1000
else:
    file = open("03_input.txt", "r")
    data = file.read().splitlines()
    fieldWidth = 30000

halfFw = int(fieldWidth/2)
field = np.zeros((fieldWidth, fieldWidth), dtype=np.uint8)
crossMin = []
crossIngs = []
crossOne = []
crossTwo = []
crossShort = []

d = data[0].split(',')
x = y = halfFw
field[y, x] = 1
for move in d:
    mLen = int(move[1:])
    dx = dy = 0
    if move[0] == 'U':
        dy = -1
    if move[0] == 'D':
        dy = 1
    if move[0] == 'R':
        dx = 1
    if move[0] == 'L':
        dx = -1
    while mLen > 0:
        mLen -= 1
        x += dx
        y += dy
        field[y, x] |= 1

d = data[1].split(',')
x = y = halfFw
for move in d:
    mLen = int(move[1:])
    dx = dy = 0
    if move[0] == 'U':
        dy = -1
    if move[0] == 'D':
        dy = 1
    if move[0] == 'R':
        dx = 1
    if move[0] == 'L':
        dx = -1
    while mLen > 0:
        mLen -= 1
        x += dx
        y += dy
        field[y, x] |= 2
        if field[y, x] == 3:
            crossIngs.append([y, x])
            crossMin.append(abs(x - halfFw) + abs(y - halfFw))

crossMin.sort()
print("Nearest crossing %i" % crossMin[0])

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

d = data[0].split(',')
x = y = halfFw
dist = 0
for move in d:
    mLen = int(move[1:])
    dx = dy = 0
    if move[0] == 'U':
        dy = -1
    if move[0] == 'D':
        dy = 1
    if move[0] == 'R':
        dx = 1
    if move[0] == 'L':
        dx = -1
    while mLen > 0:
        mLen -= 1
        dist += 1
        x += dx
        y += dy
        if field[y, x] == 3:
            a = 0
            for (i, j) in crossIngs:
                a += 1
                if y == i and x == j:
                    crossOne.append([a, dist])

d = data[1].split(',')
x = y = halfFw
dist = 0
for move in d:
    mLen = int(move[1:])
    dx = dy = 0
    if move[0] == 'U':
        dy = -1
    if move[0] == 'D':
        dy = 1
    if move[0] == 'R':
        dx = 1
    if move[0] == 'L':
        dx = -1
    while mLen > 0:
        mLen -= 1
        dist += 1
        x += dx
        y += dy
        if field[y, x] == 3:
            a = 0
            for (i, j) in crossIngs:
                a += 1
                if y == i and x == j:
                    crossTwo.append([a, dist])

crossOne.sort()
crossTwo.sort()
for i in range(len(crossOne)):
    crossShort.append((crossOne[i][1] + crossTwo[i][1]))

crossShort.sort()
print("Shortest path %i" % crossShort[0])
end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
