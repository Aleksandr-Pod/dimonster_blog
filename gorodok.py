from turtle import *

def kvadrat(a, b, c):
  fillcolor(c)
  begin_fill()
  forward(a)
  left(90)
  forward(b)
  left(90)
  forward(a)
  left(90)
  forward(b)
  left(90)
  end_fill()

def trykut(a, c):
  fillcolor(c)
  begin_fill()
  forward(a)
  left(120)
  forward(a)
  left(120)
  forward(a)
  left(120)
  end_fill()

kvadrat(100, 200, "green")
penup()
goto(0, 200)
pendown()

trykut(100, "yellow")

penup()
goto(-250, 0)
pendown()
kvadrat(200, 100, "blue")

trykut(200, "yellow")

exitonclick()