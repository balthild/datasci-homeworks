import math
import turtle


class Turtle(turtle.Turtle):
    def jump(self, x: int, y: int):
        pos = self.pos()
        self.goto(pos[0] + x, pos[1] + y)

    def rounded_trapezoid(self, width: int, height: int, angle: int):
        self.begin_fill()

        self.forward(width)
        self.circle(4, 90 - angle)
        self.forward(height)
        self.circle(4, 90 + angle)
        self.forward(width + 2 * height * math.sin(math.radians(angle)))
        self.circle(4, 90 + angle)
        self.forward(height)
        self.circle(4, 90 - angle)

        self.end_fill()


t = Turtle()
t.penup()
t.speed(100)

# Draw triangle
t.color("orange")
t.begin_fill()
for _ in range(3):
    t.forward(200)
    t.circle(20, 120)
t.end_fill()

# Draw "!"
t.color("white")
t.jump(90, 20)
t.rounded_trapezoid(20, 20, 0)
t.jump(0, 40)
t.rounded_trapezoid(20, 90, 1)

t.goto(200, 200)

turtle.done()
