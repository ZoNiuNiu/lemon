import turtle

t= turtle.Pen()

my_colors = ['red','green','yellow','black']

t.width(5)
t.speed(4)

for i in range(10):
    t.penup()
    t.goto(0, -10*i)
    t.pendown()
    t.color(my_colors[i%4])
    t.circle(20 + i*10)