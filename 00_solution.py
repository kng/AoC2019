import time
simple = True
verbose = 1

if simple:
    data = '123'
else:
    file = open('00_input.txt', 'r')
    data = file.read().splitlines()  # strip()


def main():
    start_time = time.time()

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
