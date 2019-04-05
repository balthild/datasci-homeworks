import turtle as t

t.color("red", "yellow")
t.speed(5)

t.begin_fill()
for _ in range(5):
    t.forward(200)
    t.left(216)
t.end_fill()

t.done()
