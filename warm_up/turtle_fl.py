import turtle as t

t.color("green", "green")

for _ in range(12):
    t.pendown()
    for _ in range(3):
        t.forward(20)
        t.left(120)
    t.penup()
    t.left(90)
    t.forward(20)
    t.right(120)

t.done()
