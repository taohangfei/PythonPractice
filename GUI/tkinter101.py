from Tkinter import *
from tkMessageBox import showinfo

def reply():
    showinfo(title='popup', message = 'Hello World')

window = Tk()
button = Button(window,text='press',command=reply)
button.pack()
window.mainloop()
