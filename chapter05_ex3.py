from jupyturtle import forward, left, right, back, make_turtle

def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)

make_turtle(delay = 0.01)
draw(10)