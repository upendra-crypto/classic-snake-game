from turtle import *
def border():
    border_box = Turtle("turtle")
    border_box.color("white")
    border_box.hideturtle()
    border_box.penup()
    border_box.goto(-303, 303)
    border_box.pendown()
    border_box.pensize(10)
    for i in range(4):
        border_box.fd(606)
        border_box.right(90)