# --- Day 3: No Matter How You Slice It ---
# https://adventofcode.com/2018/day/3

import re
import numpy as np

file = open("03_input.txt", "r")
data = file.read().splitlines()
mx = np.zeros((1010, 1010))
p = re.compile(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
maxy = 0
maxx = 0

for row in data:
    a = p.split(row)
    # print(a)
    startx = int(a[2])
    widthx = int(a[4])
    starty = int(a[3])
    widthy = int(a[5])
    x = startx + widthx
    y = starty + widthy
    mx[startx:startx+widthx, starty:starty+widthy] += 1
    if x > maxx:
        maxx = x
    if y > maxy:
        maxy = y

print((mx > 1).sum())

for row in data:
    a = p.split(row)
    startx = int(a[2])
    widthx = int(a[4])
    starty = int(a[3])
    widthy = int(a[5])
    x = startx + widthx
    y = starty + widthy
    ts = (mx[startx:startx+widthx, starty:starty+widthy] > 0).all() and\
         (mx[startx:startx+widthx, starty:starty+widthy] < 2).all()
    if ts:
        print(a[1])
