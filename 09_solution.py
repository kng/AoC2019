import time
simple = False
verbose = 0  # 0 = quiet, 1 = some info, 2 = babbling

if simple:
    # outputs a copy of itself
    data = "109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99"
    # output a 16 digit number
    # data = "1102,34915192,34915192,7,4,7,99,0"
    # output a large number
    # data = "104,1125899906842624,99"
else:
    file = open("09_input.txt", "r")
    data = file.read()


def main():
    start_time = time.time()

    result = computer(1)
    print("part 1 result: %i" % result)

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    result = computer(2)
    print("part 2 result: %i" % result)

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


def pad(s):
    o = [int(x) for x in str(s)]
    return o[::-1] + [0] * abs((len(o)-5))


def getprm(op, i, base, d):
    if op == 1:
        p = d[i]
    elif op == 2:
        p = d[base + d[i]]
    else:
        p = d[d[i]]
    return p


def getptr(op, i, base, d):
    if op == 1:
        p = i
    elif op == 2:
        p = base + d[i]
    else:
        p = d[i]
    return p


def computer(inp):
    d = [int(n) for n in data.split(',')]  # always run the program from scratch
    i = 0
    out = 0
    base = 0
    ptr = p1 = p2 = 0
    while i < len(d):
        try:
            op = pad(d[i])
            if verbose > 1:
                print("op: " + str(op))
            if op[0] == 1 and op[1] == 0:  # add # # dst
                p1 = getprm(op[2], i + 1, base, d)
                p2 = getprm(op[3], i + 2, base, d)
                ptr = getptr(op[4], i + 3, base, d)
                d[ptr] = p1 + p2
                i += 4
            elif op[0] == 2 and op[1] == 0:  # mul # # dst
                p1 = getprm(op[2], i + 1, base, d)
                p2 = getprm(op[3], i + 2, base, d)
                ptr = getptr(op[4], i + 3, base, d)
                d[ptr] = p1 * p2
                i += 4
            elif op[0] == 3 and op[1] == 0:  # load # dst
                ptr = getptr(op[2], i + 1, base, d)
                d[ptr] = inp
                if verbose > 0:
                    print("load %i to addr %i" % (d[ptr], ptr))
                i += 2
            elif op[0] == 4 and op[1] == 0:  # output src
                ptr = getptr(op[2], i + 1, base, d)
                out = d[ptr]
                if verbose > 0:
                    print("out %i from addr %i" % (out, d[i+1]))
                i += 2
            elif op[0] == 5 and op[1] == 0:  # jump-if-true # pp
                p1 = getprm(op[2], i + 1, base, d)
                p2 = getprm(op[3], i + 2, base, d)
                if p1 != 0:
                    i = p2
                else:
                    i += 3
            elif op[0] == 6 and op[1] == 0:  # jump-if-false # pp
                p1 = getprm(op[2], i + 1, base, d)
                p2 = getprm(op[3], i + 2, base, d)
                if p1 == 0:
                    i = p2
                else:
                    i += 3
            elif op[0] == 7 and op[1] == 0:  # less # # dst
                p1 = getprm(op[2], i + 1, base, d)
                p2 = getprm(op[3], i + 2, base, d)
                ptr = getptr(op[4], i + 3, base, d)
                if p1 < p2:
                    d[ptr] = 1
                else:
                    d[ptr] = 0
                i += 4
            elif op[0] == 8 and op[1] == 0:  # equals # # dst
                p1 = getprm(op[2], i + 1, base, d)
                p2 = getprm(op[3], i + 2, base, d)
                ptr = getptr(op[4], i + 3, base, d)
                if p1 == p2:
                    d[ptr] = 1
                else:
                    d[ptr] = 0
                i += 4
            elif op[0] == 9 and op[1] == 0:  # set relative base
                ptr = getptr(op[2], i + 1, base, d)
                base += d[ptr]
                if verbose > 0:
                    print("base %i" % base)
                i += 2
            elif op[0] == 9 and op[1] == 9:
                if verbose > 0:
                    print("end")
                    if simple:
                        print(d)
                return out
            else:
                i += 1
        except IndexError:
            need_i = max(d[i + 1], ptr)
            if verbose > 1:
                print("need more: %i" % need_i)
            curr_len = len(d) - 1
            if curr_len > 1500:
                assert False
            for z in range(need_i - curr_len + 1):
                d.append(0)

    print("program ran out!")
    return -1


main()

