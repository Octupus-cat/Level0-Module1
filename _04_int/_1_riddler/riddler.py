from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    messagebox.showinfo(message='in this game you will be asked 4 riddles from The Hobbit. After all the riddles have been asked, you will be told how many you got right. good luck!')
# Write a python program that asks the user a minimum of 3 riddles.
    score = 0
    riddle1 = simpledialog.askstring(title='riddle 1', prompt='what has roots as nobody sees, is taller than trees, up, up, up it grows, and yet never grows?')
    if riddle1 == 'a mountain':
        score += 1
    riddle2 = simpledialog.askstring(title='riddle 2', prompt='thirty white horses on a red hill. first they champ, then they stamp, then they stand still.')
    if riddle2 == 'teeth':
        score += 1
    riddle3 = simpledialog.askstring(title='riddle 3', prompt='a box without hinges, key or lid, yet golden treasure inside is hid.')
    if riddle3 == 'an egg':
        score += 1
    riddle4 = simpledialog.askstring(title='last riddle', prompt='voiceless it cries, wingless flutters, toothless bites, mouthless mutters.')
    if riddle4 == 'the wind':
        score += 1
    messagebox.showinfo(message='you got '+str(score)+'/4 questions right! good job.')
    window.mainloop()
# You can look at riddles.com if you don't already know any riddles.

# Collect the response of each riddle from the user and compare their
# answers to the correct answer.

# Use a variable to keep track of the correctly answered riddles

# After all the riddles have been asked, tell the user how many they got correct
