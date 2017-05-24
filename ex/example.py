import turtle

s = turtle.Screen()
t= turtle.Turtle(shape='turtle')
t.pensize(3)

t.pencolor('yellow')

x=-100
y=100

t.penup()
t.goto(x,y)
t.pendown()

t.circle(100)

t.penup()
t.goto(x-60.62, y+65)
t.pendown()
t.setheading(-60)
t.circle(70,120)
t.left(120)
t.forward(120)

t.penup()
t.goto(x-40,y+130)
t.pendown()
t.dot(30)

t.penup()
t.goto(x+40, y+130)
t.pendown()
t.dot(30)
