# --- Day 1: Chronal Calibration ---
# https://adventofcode.com/2018/day/1

import numpy as np
import time
simple = False

start_time = time.time()

if simple:
    data = ['+7', '+7', '-2', '-7', '-4']
else:
    file = open("01_input.txt", "r")
    data = file.readlines()

skew = np.array([], dtype=np.int32)
freq = np.array([], dtype=np.int32)
curr = 0

for line in data:
    val = int(line)
    skew = np.append(skew, val)
    curr += val

print("First part: %i" % curr)
curr = 0

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

found = False
while not found:
    for line in skew:
        curr += line
        if curr in freq:
            found = True
            break
        freq = np.append(freq, curr)

print("Second answer: %i" % curr)
end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
