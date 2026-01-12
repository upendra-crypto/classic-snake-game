from turtle import Turtle
UP=90
DOWN=270
LEFT=180
RIGHT=0
MOVE_DIST = 20
pos = [(0, 0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.segments = []
        for p in pos:
            self.add_segement(p)
        self.segments[0].color("red")
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DIST)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading()!= UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading()!= RIGHT:
            self.head.setheading(LEFT)
    def add_segement(self,position):
        snake = Turtle("circle")
        snake.color("white")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)
    def extend(self):
        self.add_segement(self.segments[-1].position())