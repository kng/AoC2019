import time
simple = False
# simple = True


def pad(s):
    o = [int(x) for x in str(s)]
    return o[::-1] + [0] * abs((len(o)-5))


start_time = time.time()

if simple:
    # data = "1,9,10,3,2,3,11,0,99,30,40,50"
    # data = "1,0,0,0,99"
    # data = "3,0,4,0,99"
    # data = "1002,4,3,4,33"
    # data = "1101,100,-1,4,0"
    # data = "3,9,8,9,10,9,4,9,99,-1,8"
    # data = "3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9"
    # data = "3,3,1105,-1,9,1101,0,0,12,4,12,99,1"
    data = "3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125," \
           "20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99,0,0"
else:
    file = open("05_input.txt", "r")
    data = file.read()

d = [int(n) for n in data.split(',')]
dLen = len(d)
i = 0

# first part input = 1, second part input = 5
inp = 5  # load instruction parameter

if simple:
    print(d)

while i < dLen:
    op = pad(d[i])
    if simple:
        print("op: " + str(op))
    if op[0] == 1 and op[1] == 0:  # add # # dst
        if simple:
            print("add")
        if op[2] == 0:
            p1 = d[d[i + 1]]
        else:
            p1 = d[i + 1]
        if op[3] == 0:
            p2 = d[d[i + 2]]
        else:
            p2 = d[i + 2]
        d[d[i + 3]] = p1 + p2
        i += 4
    elif op[0] == 2 and op[1] == 0:  # mul # # dst
        if simple:
            print("mul")
        if op[2] == 0:
            p1 = d[d[i + 1]]
        else:
            p1 = d[i + 1]
        if op[3] == 0:
            p2 = d[d[i + 2]]
        else:
            p2 = d[i + 2]
        d[d[i + 3]] = p1 * p2
        i += 4
    elif op[0] == 3 and op[1] == 0:  # load # dst
        if simple:
            print("load")
        d[d[i + 1]] = inp
        i += 2
    elif op[0] == 4 and op[1] == 0:  # output src
        print("out %i" % d[d[i + 1]])
        i += 2
    elif op[0] == 5 and op[1] == 0:  # jump-if-true # pp
        if simple:
            print("jump if true")
        if op[2] == 0:
            p1 = d[d[i + 1]]
        else:
            p1 = d[i + 1]
        if op[3] == 0:
            p2 = d[d[i + 2]]
        else:
            p2 = d[i + 2]
        if p1 != 0:
            i = p2
        else:
            i += 3
    elif op[0] == 6 and op[1] == 0:  # jump-if-false # pp
        if simple:
            print("jump if false")
        if op[2] == 0:
            p1 = d[d[i + 1]]
        else:
            p1 = d[i + 1]
        if op[3] == 0:
            p2 = d[d[i + 2]]
        else:
            p2 = d[i + 2]
        if p1 == 0:
            i = p2
        else:
            i += 3
    elif op[0] == 7 and op[1] == 0:  # less # # dst
        if simple:
            print("less")
        if op[2] == 0:
            p1 = d[d[i + 1]]
        else:
            p1 = d[i + 1]
        if op[3] == 0:
            p2 = d[d[i + 2]]
        else:
            p2 = d[i + 2]
        if p1 < p2:
            d[d[i + 3]] = 1
        else:
            d[d[i + 3]] = 0
        i += 4
    elif op[0] == 8 and op[1] == 0:  # equals # # dst
        if simple:
            print("equals")
        if op[2] == 0:
            p1 = d[d[i + 1]]
        else:
            p1 = d[i + 1]
        if op[3] == 0:
            p2 = d[d[i + 2]]
        else:
            p2 = d[i + 2]
        if p1 == p2:
            d[d[i + 3]] = 1
        else:
            d[d[i + 3]] = 0
        i += 4
    elif op[0] == 9 and op[1] == 9:
        print("end")
        i = dLen
    else:
        i += 1

if simple:
    print(d)

end_time = time.time()
print("time elapsed: %s" % (end_time - start_time))
