def takeOneDown(x):
    print("{0} bottles of beer on the wall, {0} bottles of beer. Take one down, pass it around, {1} bottles of beer on the wall.".format(x, x-1))

for i in range (99, 0, -1): takeOneDown(i)