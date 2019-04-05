import turtle

t = turtle.Turtle()
t.penup()

for _ in range(7):
    for _ in range(5):
        t.dot()
        t.forward(20)
    t.back(100)
    t.right(90)
    t.forward(20)
    t.left(90)

turtle.done()
