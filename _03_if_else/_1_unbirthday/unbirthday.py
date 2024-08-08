import turtle
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    day = "08-08"

    answer = simpledialog.askstring(title='birthday', prompt='what day is your birthday?')

    if answer == day:
        messagebox.showinfo(message='Happy birthday!!!')
    else:
        messagebox.showinfo(mesage='Happy UNbirthday!!!')
