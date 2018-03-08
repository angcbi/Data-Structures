# -*- coding:utf-8 -*-
import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)

    myTurtle.right(90)
    drawSpiral(myTurtle, lineLen-3)

drawSpiral(myTurtle, 100)
myWin.exitonclick()