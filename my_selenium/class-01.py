import turtle

n = 500
turtle.penup()
turtle.goto(-450, 150)
turtle.pendown()
turtle.pencolor("blue")

for i in range(500):
    n = n - 1
    # n -= 1
    turtle.speed(100)
    turtle.fd(n)
    turtle.right(90)

turtle.pendone()