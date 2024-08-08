import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    radius = simpledialog.askinteger(title='question', prompt='please enter the radius of your circle (in pixels) to calculate its area')
    
    # Make a new turtle
    bob = turtle.Turtle()
    bob.shape('turtle')
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    bob.circle(radius)
    # Call the turtle .penup() method
    bob.penup()
    # Move your turtle to a new x,y position using .goto()
    bob.goto(-50, -100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = math.pi*radius*radius
    # Write the area of your circle using the turtle .write() method
    # my_turtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    bob.write("arg = " + str(area), move=True, align='left', font=('Arial', 10, 'normal'))
    # Hide your turtle
    bob.color('white')
    bob.speed(1)
    bob.circle(500)
    bob.hideturtle()
    # Call turtle.done()
    bob.done()
