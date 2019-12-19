# -*- coding: utf-8 -*-
#! /usr/bin/py -3

from tkinter import *
import server_file_gui
import client_file_gui


def sfg():
    root.destroy()
    server_file_gui.start()

def cfg():
    root.destroy()
    client_file_gui.start()

def greet():
    global root
    root = Tk()
    root.title("D-Netflix")
    l1 = Label(root, text="D-Netflix", bg="pale green", font = ("Symbol", 26))
    l1.pack(side=TOP, fill=X)
    l2 = Label(root, text="An application of Stack and Queue.", bg="aquamarine", font = ("Purisa", 16))
    l2.pack(side=BOTTOM, fill=X)
    
    b1 = Button(root, text="SERVER", bg="RoyalBlue1", fg="red", cursor="star", command=sfg)
    b1.pack(side=LEFT, fill=X, expand=True)
    b2 = Button(root, text="CLIENT", bg="RoyalBlue1", fg="red", cursor="star", command=cfg)
    b2.pack(side=RIGHT, fill=X, expand=True)

    root.mainloop()

if __name__ == "__main__":
    greet()


