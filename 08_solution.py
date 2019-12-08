import time
simple = False
verbose = 0
start_time = time.time()

if simple:
    # part 1
    # data = "003456789012"
    # width = 3
    # height = 2
    # part 2
    data = "0222112222120000"
    width = 2
    height = 2
else:
    file = open("08_input.txt", "r")
    data = file.read()
    width = 25
    height = 6

d = list(map(int, data.strip()))

layers = []
for ofs in range(0, len(d), width * height):
    layers.append(d[ofs:width * height + ofs])

lowest = width * height
lowLayer = 0
for i in range(len(layers)):
    if verbose > 1:
        print("layer %i z %i = %s" % (i, layers[i].count(0), str(layers[i])))
    if layers[i].count(0) < lowest:
        lowest = layers[i].count(0)
        lowLayer = i

if verbose > 0:
    print("lowest layer %i" % lowLayer)

print("code: %i" % (layers[lowLayer].count(1) * layers[lowLayer].count(2)))

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

image = width * height * [2]
for i in range(len(layers)):
    for j in range(width * height):
        if image[j] == 2 and layers[i][j] < 2:
            image[j] = layers[i][j]

for i in range(height):
    print(image[i*width:(i+1)*width])

end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
