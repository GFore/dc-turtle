from turtle import *

def square(size):
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)
    right(90)
    forward(size)

def unsquare(size):
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)
    left(90)
    forward(size)

speed(6)
square(200)
right(180)
speed(6)
color('white')
unsquare(200)
# forward(300)
# right(180)
# color('green', 'blue')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()
input()

