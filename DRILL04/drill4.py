import turtle

count = 5
while (count>0) :
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.left(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    count -= 1

turtle.forward(500)
turtle.right(90)

count = 5
while(count>0):
    turtle.forward(500)
    turtle.penup()
    turtle.backward(500)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    count -= 1

turtle.forward(500)

turtle.exitonclick()