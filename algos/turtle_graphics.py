import turtle

myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        print lineLen
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()

# import turtle
# wn = turtle.Screen()        # creates a graphics window
# alex = turtle.Turtle()      # create a turtle named alex
# alex.forward(150)           # tell alex to move forward by 150 units
# alex.left(90)               # turn by 90 degrees
# alex.forward(75)            # complete the second side of a rectangle
# wn.exitonclick()
# def draw_square():
#     window = turtle.Screen()
#     window.bgcolor("red")
#     brad = turtle.Turtle()
#     brad.forward(100)
#
# draw_square()
