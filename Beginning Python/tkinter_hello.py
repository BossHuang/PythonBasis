__author__ = 'leihuang'

from Tkinter import *

def hello():
    print "hello, Tkinter"

win = Tk()
win.title("Hello, Tkinter")

btn = Button(win, text="hello ", command=hello)
btn.pack(expand=YES, fill=BOTH)

mainloop()