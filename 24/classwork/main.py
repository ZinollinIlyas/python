import turtle

turtle.color('red', 'yellow')
turtle.begin_fill()
for i in range(2):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()
turtle.done()
print(turtle.pos())
print(turtle.color())
