import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    bob = turtle.Turtle()
    bob.shape('turtle')
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title='shape', prompt='What shape do you want to draw?')
    # Draw the shape requested by the user using if-elif-else statements
    if shape == 'circle':
        bob.circle(200)
        bob.penup()
        bob.color('white')
        bob.circle(400)
    elif shape == 'square':
        for i in range(4):
            bob.right(90)
            bob.forward(200)
        bob.penup()
        bob.color('white')
        bob.circle(400)
    elif shape == 'rectangle':
        for i in range(2):
            bob.forward(400)
            bob.right(90)
            bob.forward(200)
            bob.right(90)
        bob.penup()
        bob.color('white')
        bob.circle(400)
    else:
        messagebox.showinfo(message='Sorry, we do not know how to draw that shape.')
    # Call the turtle .done() method

