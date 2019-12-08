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

d = list(data)
if d[-1] == '\n':
    del(d[-1])
d = [int(n) for n in list(d)]

image = width * height * [0]
layers = []
zeroes = []
i = 0
zero = 0
for px in d:
    if verbose > 2:
        print("x = %i, y = %i, px = %i" % (x, y, px))
    image[i] = px
    if px == 0:
        zero += 1
    i += 1
    if i == width * height:
        if verbose > 2:
            print("layer: %s" % str(image))
        layers.append(image.copy())
        zeroes.append(zero)
        zero = 0
        i = 0

i = 0
lowest = width * height
lowlayer = -1
while i < len(layers):
    if verbose > 1:
        print("layer %i z%i = %s" % (i, zeroes[i], str(layers[i])))
    if zeroes[i] < lowest:
        lowest = zeroes[i]
        lowlayer = i
    i += 1

if verbose > 0:
    print("lowest layer %i" % lowlayer)

sum1 = 0
sum2 = 0
for i in layers[lowlayer]:
    if i == 1:
        sum1 += 1
    if i == 2:
        sum2 += 1

print("code: %i" % (sum1 * sum2))

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

image = width * height * [2]

i = 0
while i < len(layers):
    j = 0
    while j < width * height:
        if image[j] == 2 and layers[i][j] < 2:
            image[j] = layers[i][j]
        j += 1
    i += 1

for i in range(height):
    print(image[i*width:(i+1)*width])

end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
