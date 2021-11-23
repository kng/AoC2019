# --- Day 4: Repose Record ---
# https://adventofcode.com/2018/day/4

import numpy as np
import re
from datetime import datetime as dt
import time

start_time = time.time()

# file = open("04_simple.txt", "r")
file = open("04_input.txt", "r")
data = file.read().splitlines()
data.sort()

g = re.compile(r'Guard #(\d+) begins shift')
s = re.compile(r'falls asleep')
w = re.compile(r'wakes up')

guard_time = {}
guard = 0
asleep = 0
for line in data:
    utc_time = dt.strptime(line[1:17], '%Y-%m-%d %H:%M')
    gn = g.findall(line)
    st = s.findall(line)
    wt = w.findall(line)
    if gn:
        guard = gn[0]
        if guard not in guard_time:
            guard_time[guard] = np.zeros(60, dtype=int)  # minute sleep array
    if st:
        asleep = utc_time.minute
    if wt:
        awake = utc_time.minute
        guard_time[guard][asleep:awake] += 1     # increase slept minute array

guard_max = 0
guard_id = 0
guard_minute = 0
for g in guard_time:
    if guard_time[g].sum() > guard_max:
        guard_max = guard_time[g].sum()
        guard_id = int(g)
        guard_minute = guard_time[g].argmax()
print("most heavy sleeper: %i, slept %i, max at %i, code = %i" %
      (guard_id, guard_max, guard_minute, guard_id * guard_minute))

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

guard_max = 0
for g in guard_time:
    if guard_time[g].max(initial=0) > guard_max:
        guard_max = guard_time[g].max(initial=0)
        guard_id = int(g)
        guard_minute = guard_time[g].argmax()
print("most reliable: %i, max %i, at minute: %i, code = %i" %
      (guard_id, guard_max, guard_minute, guard_id * guard_minute))
end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
