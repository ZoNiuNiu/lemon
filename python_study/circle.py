import turtle

t= turtle.Pen()

my_colors = ['red','green','yellow','black']

t.width(3)
t.speed(1)

for i in range(10):
    t.circle(20 + i*10)

