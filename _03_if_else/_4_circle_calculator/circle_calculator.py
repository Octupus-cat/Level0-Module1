from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    radius = simpledialog.askstring(title='radius', prompt='What is the radius of your circle?')
# Write a Python program that asks the user for the radius of a circle.
    calculation = simpledialog.askstring(title='area or circumference', prompt='Would you like to calculate the area or circumference of your circle?')
# Next, ask the user if they would like to calculate the area or circumference of a circle.
    if calculation == 'area':
        answer = int(radius)*int(radius)
        bob = answer*math.pi
        messagebox.showinfo(message='the area of a circle that has a radius of '+str(radius)+' is '+str(bob)+'.')
    elif calculation == 'circumference':
        answer2 = int(math.pi)*int(radius)
        joe = answer2*math.pi
        messagebox.showinfo(message='the circumference of a circle that has a radius of '+str(radius)+' is '+str(answer2)+'.')
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.
    window.mainloop()
# Area = πr^2
# Circumference = 2πr
