from turtle import *

def square(size):
    color('black')
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)

def unsquare(size):
    color('white')
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)

def star():
    color('green', 'blue')
    begin_fill()
    cnt = 0
    while cnt < 36:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
        cnt += 1
    end_fill()

speed(0)        # fastest speed
x = xcor()      # save position for move back to center
y = ycor()

for i in range(80):
    square(200)
    right(180)
    unsquare(200)
    right(25)

setpos(x+100, y-20)     # move to position to draw star in middle
star()
input()  # dummy input to keep window open