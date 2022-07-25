import turtle
import time

from cv2 import circle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(2)
t.hideturtle()
t.goto(0,-10)

t.pensize(30)
t.color("red")
t.begin_fill()
t.left(140)
t.forward(180)
t.circle(-90,200)
t.setheading(60)
t.circle(-90,200)
t.forward(178)
t.end_fill()

t.penup()
t.goto(-120,200)
t.pendown()
t.color("white")
t.write(" TE AMO LILIANA ",font=("vertana",23,"bold"))
t.end_fill()
t.penup()
t.goto(-50,160)
t.pendown()
t.color("white")
t.write(" NUNCA ",font=("vertana",23,"bold"))
t.end_fill()
t.penup()
t.goto(-90,110)
t.pendown()
t.color("white")
t.write("LO OLVIDES ",font=("vertana",23,"bold"))
t.end_fill()
time.sleep(5)





