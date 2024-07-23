from turtle import Turtle
POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.segment = []
        for i in POSITION:
            tim = Turtle("square")
            tim.penup()
            tim.color("white")
            tim.goto(i)
            self.segment.append(tim)
            self.head = self.segment[0]

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)
        if self.head.xcor()>300 or self.head.ycor()>300:
            print("Yup")


    def Up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)


    def Down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def Left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def Right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def add_body(self):
        tim = Turtle("square")
        tim.penup()
        tim.color("white")
        self.segment.append(tim)

        
