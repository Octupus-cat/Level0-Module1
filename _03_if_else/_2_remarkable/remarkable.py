from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    name = simpledialog.askstring(title='question', prompt='type in the name of someone to learn something remarkable about them (bob, joe, or fred)')
    if name == 'bob':
        messagebox.showinfo(message='bob is a turtle')
    elif name == 'joe':
        messagebox.showinfo(message='joe likes cheese')
    elif name == 'fred':
        messagebox.showinfo(message='fred goes to hogwarts with his twin brother george, and they created a swamp in a hallway once')
    else:
        messagebox.showinfo(message='we do not know that person, sorry. try using lowercase letters.')
    window.mainloop()
