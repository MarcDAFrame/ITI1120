import turtle 
s=turtle.Screen() 
t=turtle.Turtle() 

# since this starts with # it is just a comment and thus ignored by python interpreter

# draw the head, i.e. circle of radius 70  
t.circle(70)

#move the pen
t.penup()
t.goto(15, 80)
t.pendown()

# draw right eye as a rectangle
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)

#move the pen
t.up()
t.goto(-15, 80)
t.pendown()

#make the pen face up
t.setheading(90) 

# draw left eye as a rectangle
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)

#make the pen
t.up()
t.goto(-15, 35)
t.pendown()

# draw a smile as a half circle
t.setheading(-45)
t.circle(30,90)
