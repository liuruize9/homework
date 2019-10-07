import turtle
turtle.setup(600,400,200,200)
turtle.bgcolor("red")
turtle.fillcolor ("yellow")
turtle.color('yellow')
#主星
turtle.begin_fill()
turtle.penup()
turtle.goto(-260,120)
turtle.pendown()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)
turtle.end_fill()
#副星1
turtle.begin_fill()
turtle.penup()
turtle.goto(-120,160)
turtle.pendown()
for i in range (5):
    turtle.forward(18)
    turtle.right(144)
turtle.end_fill()
#2
turtle.begin_fill()
turtle.penup()
turtle.goto(-80,120)
turtle.pendown()
for i in range (5):
    turtle.forward(18)
    turtle.right(144)
turtle.end_fill()
#3
turtle.begin_fill()
turtle.penup()
turtle.goto(-80,60)
turtle.pendown()
for i in range (5):
    turtle.forward(18)
    turtle.right(144)
turtle.end_fill()
#4
turtle.begin_fill()
turtle.penup()
turtle.goto(-120,20)
turtle.pendown()
for i in range (5):
    turtle.forward(18)
    turtle.right(144)
turtle.end_fill()

