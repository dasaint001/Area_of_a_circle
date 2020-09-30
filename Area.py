import math
import turtle

# create screen
screen = turtle.Screen()
# take input from screen
r = float(screen.textinput("Area of Circle", "Enter the radius of the circle in meter: "))
# draw circle of radius r
t=turtle.Turtle()
t.fillcolor('orange')
t.begin_fill()
t.circle(r)
t.end_fill()
turtle.penup()
# calculate area
area = math.pi * r * r
# color,style and position of text
turtle.color('deep pink')
style = ('Courier', 10, 'italic')
turtle.setpos(-20,-20)
# display area of circle with radius r
turtle.write(f"Area of the circle with radius {r} meter is {area} meter^2", font=style, align='center')
# hide the turtle symbol
turtle.hideturtle()
# don't close the screen untill click on close
turtle.getscreen()._root.mainloop()
