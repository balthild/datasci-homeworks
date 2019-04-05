import turtle


def draw_group(group):
    for (color, radius) in group:
        t.color(color)
        t.circle(radius)


t = turtle.Turtle()
t.speed(100)
t.screen.bgcolor("black")

for _ in range(10):
    draw_group([
        ("yellow", 50),
        ("white", 52),
        ("yellow", 54),
        ("white", 56),
        ("yellow", 58),
        ("white", 60),
    ])
    t.right(36)

for _ in range(10):
    draw_group([
        ("blue", 66),
        ("white", 67),
        ("blue", 70),
        ("white", 71),
        ("blue", 74),
        ("white", 75),
        ("blue", 78),
        ("white", 79),
    ])
    t.right(36)

for _ in range(10):
    draw_group([
        ("pink", 48),
        ("orange", 49),
        ("pink", 62),
        ("orange", 63),
        ("pink", 81),
    ])
    t.right(36)

t.right(18)

for _ in range(10):
    draw_group([
        ("pink", 36),
        ("orange", 37),
        ("pink", 60),
        ("orange", 61),
    ])
    t.right(36)

turtle.done()
