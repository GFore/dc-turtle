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
    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()

speed(10)
for i in range(20):
    square(200)
    right(180)
    unsquare(200)
    right(25)
# forward(300)
# right(180)
for i in range(5):
    star()
    right(45)
    penup()
    forward(200)
    pendown()
# done()
input()

