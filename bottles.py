def takeOneDown(x):
    print("{0} bottle{2} of beer on the wall, {0} bottle{2} of beer.\nTake one down, pass it around, {1} bottle{3} of beer on the wall.".format(x, x-1, 's' if x>1 else '', 's' if x>2 else ''))

for i in range (99, 0, -1): takeOneDown(i)