import turtle # imports turtle package
pen = turtle.Pen() 

pen.color('Blue') # sets the pen color to blue
pen.setheading(45) #sets the orientation of turtle to an angle 45
pen.forward(70) # moves the turtle forward with the specified distance of 70
pen.setheading(315) #sets the orientation of turtle to an angle 315
pen.forward(100) #moves the turtle forward with the specified distance 100
pen.setheading(225)#sets the orientation of turtle to an angle 225
pen.forward(70) #moves the turtle forward with the specified distance of 70
pen.penup() # pulls up the pen, no drawing while the pen moves
pen.goto(0, 0) # moves the pen to an absolute direction, without drawing a line
pen.pendown() # pulls the pen down, will draw lines while moving
pen.color('Red') # sets the pen color to red
pen.showturtle() # makes the turtle visible
pen.setheading(135) #sets the orientation of turtle to an angle 315
pen.forward(70) #moves the turtle forward with the specified distance of 70
pen.setheading(225) #sets the orientation of turtle to an angle 225
pen.forward(100) #moves the turtle forward with the specified distance 100
pen.setheading(315) #sets the orientation of turtle to an angle 315
pen.forward(70) #moves the turtle forward with the specified distance of 70

turtle.done()  # makes the graphics stay
