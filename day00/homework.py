from turtle import *



#i want to draw a house

#step1 draw a square
speed(30)
width(7)
color ("purple")
begin_fill()
forward (200)

left(90)

forward(200)

left(90)

forward (200)

left(90)

forward(200)

left(90)
end_fill()
#end of square

#drawimg a door
forward(70)
color("light blue")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

#roof
color("pink")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(60, 130)
pendown()

#windows
color("yellow")
begin_fill()
right(60)
forward(40)
right(90)
forward(50)
right(90)
forward(40)
right(90)
forward(50)

penup()
goto(140, 130)
pendown()

left(90)
forward(40)
left(90)
forward(50)
left(90)
forward(40)
left(90)
forward(50)
end_fill()

exitonclick()
