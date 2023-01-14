from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(x, y)

    def go_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def go_down(self):
        if self.ycor() > -250:
            self.backward(20)
