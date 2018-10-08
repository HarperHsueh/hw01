import turtle
import time


def drawflag():
    turtle.pensize(5)
    turtle.color("red")
    turtle.speed(5)
    turtle.penup()
    turtle.goto(-450,300)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(900)
        turtle.right(90)
        turtle.forward(600)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
def drawstar():
#star1
    turtle.goto(-395,195)
    turtle.pendown()
    turtle.color("yellow")
    turtle.pensize(7)
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(100)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
#star2    
    turtle.goto(-265,255)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.pensize(7)
    turtle.right(36)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
#star3    
    turtle.goto(-210,215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.pensize(7)
    turtle.right(54)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
#star4        
    turtle.goto(-220,160)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.pensize(7)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()
    turtle.penup()
#star5    
    turtle.goto(-250,115)
    turtle.pendown()
    turtle.begin_fill()
    turtle.color("yellow")
    turtle.pensize(7)
    turtle.right(36)
    for i in range(5):
        turtle.forward(30)
        turtle.right(144)
    turtle.end_fill()

    turtle.hideturtle()

    
drawflag()
drawstar()
