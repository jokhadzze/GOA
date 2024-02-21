from turtle import *

speed(80)
width(7)
#square
color ("light blue")
penup()
goto(180, 100)
pendown()

begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()

#doors
color("pink")
penup()
goto(230, 170)
pendown()

begin_fill()
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(230, 200)
pendown()

#windows
color("purple")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)

penup()
goto(280, 200)
pendown()


forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()

penup()
goto(335, 255)
pendown()

#roof
color("yellow")
begin_fill()
left(50)
forward(100)
left(80)
forward(100)
left(140)
forward(150)
end_fill()

#square
color ("light blue")
penup()
goto(-20, 100)
pendown()

begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()

#doors
color("pink")
penup()
goto(30, 170)
pendown()

begin_fill()
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(30, 200)
pendown()

#windows
color("purple")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)

penup()
goto(80, 200)
pendown()


forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()

penup()
goto(135, 255)
pendown()

#roof
color("yellow")
begin_fill()
left(50)
forward(100)
left(80)
forward(100)
left(140)
forward(150)
end_fill()

#square
color ("light blue")
penup()
goto(180, -200)
pendown()

begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()

#doors
color("pink")
penup()
goto(230, -130)
pendown()

begin_fill()
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(230, -100)
pendown()

#windows
color("purple")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)

penup()
goto(280, -100)
pendown()


forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()

penup()
goto(335, -45)
pendown()

#roof
color("yellow")
begin_fill()
left(50)
forward(100)
left(80)
forward(100)
left(140)
forward(150)
end_fill()
#square
color ("light blue")
penup()
goto(-20, -200)
pendown()

begin_fill()
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
forward(150)
left(90)
end_fill()

#doors
color("pink")
penup()
goto(30, -130)
pendown()

begin_fill()
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(70)
end_fill()

penup()
goto(30, -100)
pendown()

#windows
color("purple")
begin_fill()
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)

penup()
goto(80, -100)
pendown()


forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
end_fill()

penup()
goto(135, -45)
pendown()

#roof
color("yellow")
begin_fill()
left(50)
forward(100)
left(80)
forward(100)
left(140)
forward(150)
end_fill()

penup()
goto(-300, 200)
pendown()

#sun
begin_fill()
circle(radius=60)
end_fill()
 
penup()
goto(-300, -100)
pendown()

#trees
color("brown")
begin_fill()
forward(50)
right(90)
forward(150)
right(90)
forward(50)
right(90)
forward(150)
right(90)
end_fill()

penup()
goto(-280, -120)
pendown()

color("green")
begin_fill()

circle(radius=80)
end_fill()

penup()
goto(-150, -170)
pendown()

color("brown")
begin_fill()
forward(30)
right(90)
forward(130)
right(90)
forward(30)
right(90)
forward(130)
right(90)
end_fill()

penup()
goto(-130, -190)
pendown()

color("green")
begin_fill()
circle(radius=40)
end_fill()

exitonclick()