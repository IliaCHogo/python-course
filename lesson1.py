from turtle import *

#we want to pain a house

#step 1: draw a square
speed(30)
width(5)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("yellow")
left(90)      
forward(100)  #height of the door
right(90)
forward(60)
right(90)
forward(100)

penup()
goto(200,200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)     
left(120)
forward(200)
end_fill()

#draw window
color("sky blue")
begin_fill()
left(30)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(90)
forward(70)
left(180)
forward(200)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()








exitonclick()































