import time
start_time = time.time()

nStart = 357253
nStop = 892942
nValid = 0
first = False

for i in range(nStart, nStop):
    n = [int(d) for d in str(i)]
    ascend = True
    doubles = False
    m = -1
    for j in n:
        if j < m:
            ascend = False
        if j == m:
            doubles = True
        m = j
    if ascend and doubles:
        nValid += 1
print("first valid: %i" % nValid)

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

nValid = 0
for i in range(nStart, nStop):
    n = [int(d) for d in str(i)]
    ascend = True
    doubles = False
    m = -1
    for j in n:
        if j < m:
            ascend = False
        if first:
            if j == m:
                doubles = True
        m = j
    if not first:
        if (n[0] == n[1] and n[1] != n[2]) \
                or (n[0] != n[1] and n[1] == n[2] and n[2] != n[3]) \
                or (n[1] != n[2] and n[2] == n[3] and n[3] != n[4]) \
                or (n[2] != n[3] and n[3] == n[4] and n[4] != n[5]) \
                or (n[3] != n[4] and n[4] == n[5]):
            doubles = True
    if ascend and doubles:
        nValid += 1

print("second valid: %i" % nValid)

end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
