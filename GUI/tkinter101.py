from Tkinter import *
from Tkinter.messagebox import showinfo

def reply():
    showinfo(title='popup', message = 'OK')

window = Tk()
button = Button(window,text='press',command=reply)
button.pack()
window.mainloop()
