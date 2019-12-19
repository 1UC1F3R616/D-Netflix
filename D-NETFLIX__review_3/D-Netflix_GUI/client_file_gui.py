#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import webbrowser
import os
import time
import list_extractor as liex
from collections import Counter
import d_netflix_gui
from tkinter import *
import tkinter.ttk
from PIL import ImageTk, Image
import tkinter.messagebox

def on_entry_click1(event):
    """function that gets called whenever entry is clicked"""
    if e1.get() == 'Username...':
       e1.delete(0, "end") # delete all the text in the entry
       e1.insert(0, '') #Insert blank for user input
       e1.config(fg = 'black')
def on_focusout1(event):
    if e1.get() == '':
        e1.insert(0, 'Username...')
        e1.config(fg = 'grey')
def on_entry_click2(event):
    """function that gets called whenever entry is clicked"""
    if e2.get() == 'Password...':
       e2.delete(0, "end") # delete all the text in the entry
       e2.insert(0, '') #Insert blank for user input
       e2.config(fg = 'black')
def on_focusout2(event):
    if e2.get() == '':
        e2.insert(0, 'Password...')
        e2.config(fg = 'grey')


def choice():

    def stats(self):

        def thorough(self):
            global client_id
            global client_pass
            def seen(self):
                root4.destroy()
            root4=Tk()
            l1=Label(root4, text="Client id: "+client_id+"\t\t"+"Client Password: "+client_pass+'\t\t'+"DateTime: "+time.ctime(), fg="blue")
            l1.grid(row=0, column=0, padx=10, pady=10)
            f = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
            ff = f.readlines()
            f.close()
            l2=Label(root4, text="Total "+str(len(ff))+" films have been watched so far.", fg="green yellow")
            l2.grid(row=1, column=0, padx=10, pady=10)
            text = [x.split('\t') for x in ff]
            frequent = [x[1].replace('\n', '') for x in text]
            counter = Counter(frequent).most_common(3)
            l3=Label(root4, text=client_id+" favourate films:", fg="gold")
            l3.grid(row=2, column=0)
            count3=3
            for x in counter:
                l4=Label(root4, text=x[0])
                l4.grid(row=count3, column=0)
                count3+=1
            b1=Button(root4, text="CLOSE", fg="red", bg="black")
            b1.grid(row=count3, column=0)
            b1.bind("<Button-1>", seen)
            root4.bind("<Return>", seen)


        def frequency(self):
            def seen(self):
                root3.destroy()
            
            root3=Tk()
            global client_id
            global client_pass
            file = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
            file_text = file.readlines()
            file.close()
            text = [x.split('\t') for x in file_text]
            frequent = [x[1].replace('\n', '') for x in text]
            l1=Label(root3, text="Frequency\t Film:::")
            l1.grid(row=0, column=0)
            count2=1
            for x in Counter(frequent):
                l2=Label(root3, text=str(Counter(frequent)[x])+'\t\t'+x, fg="brown")
                l2.grid(row=count2, column=0)
                count2+=1
            b1=Button(root3, text="CLOSE", fg="red", bg="black")
            b1.bind("<Button-1>", seen)
            b1.grid(row=count2, column=0, columnspan=2)
            root3.bind("<Return>", seen)
        
        root2=Tk()
        root2.title("^_^FILM STATS^_^")
        root2.geometry("400x60")
        b1=Button(root2, text="WATCH FREQUENCY", fg="green", bg="CadetBlue1")
        b1.pack(fill=BOTH)
        b1.bind("<Button-1>", frequency)
        b2=Button(root2, text="THOROUGH STATS", fg="green", bg="CadetBlue1")
        b2.pack(fill=BOTH)
        b2.bind("<Button-1>", thorough)
        

    def history(self):
        global client_id
        global client_pass
        def seen(self):
            root2.destroy()
        file = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
        file_text = file.readlines()
        file.close()
        file_text.reverse()
        root2=Tk()
        root2.title("HISTORY")
        l1=Label(root2, text="DateTime                 \tFilm:::")
        l1.grid(row=0, column=0)
        count=1
        for line in file_text:
            l2=Label(root2, text=line, fg="brown")
            l2.grid(row=count, column=0)
            count+=1
        b1 = Button(root2, text="CLOSE", fg="red", bg="black", relief="groove")
        b1.grid(row=count, column=0, columnspan=2)
        b1.bind("<Button-1>", seen)
        root2.bind("<Return>", seen)

    def watch(self):

        def see(self):
            global client_id
            global client_pass
            title=e1.get()
            root2.geometry("450x250")
            file = open('dsap_92det.txt', "r")
            file_text = file.readlines()
            file.close()
            file_r_text = liex.cleaner(file_text)
            for line in file_r_text:
                if line[1]==title:
                    file = open("clients/"+client_id+'_'+client_pass+'.txt', "a+")
                    file.write(time.ctime()+'\t '+title+'\n')
                    collect = open("collective.txt", "a+")
                    collect.write(time.ctime()+'\t '+title+'\n')
                    collect.close()
                    file.close()
                    webbrowser.open(line[0])
                    root2.destroy()
                    break
            else:
                tkinter.messagebox.showinfo("Film Not Present", title+" is not present")
                root2.destroy()
                watch(self)
        
        root2 = Tk()
        root.title("FILM TIME")
        l1 = Label(root2, text="TITLE", padx=10, pady=10)
        l1.grid(row=0, column=0)
        e1 = Entry(root2, width=20)
        e1.grid(row=0, column=1, columnspan=2)
        e1.focus_set()
        b1 = Button(root2, text="Lit", fg="red", bd=1, padx=10, pady=10)
        b1.grid(row=1, column=0, rowspan=2, columnspan=2)
        b1.bind("<Button-1>", see)
        root2.bind("<Return>", see)

        
    
    root=Tk()
    root.title("CLIENT MAIN-MENU")

    def seen(self):
        root.destroy()
        d_netflix_gui.greet()

    img = ImageTk.PhotoImage(Image.open("watch1.png"))
    #b1 = Button(root, text="WATCH", bg="dark violet", fg="snow", cursor="mouse", relief="raised", command=watch)
    b1 = Button(root, image=img, cursor="mouse", relief="raised", padx=10, pady=20)
    b1.bind("<Button-1>", watch)
    b1.image=img
    b1.grid(row=0, column=0)
    #b2 = Button(root, text="HISTORY", bg="dark violet", fg="snow", cursor="mouse", relief="raised")
    img = ImageTk.PhotoImage(Image.open("history1.png"))
    b2 = Button(root, image=img, cursor="mouse", relief="raised", padx=10, pady=20)
    b2.bind("<Button-1>", history)
    b2.image=img
    b2.grid(row=1, column=0)
    #b3 = Button(root, text="STATS", bg="dark violet", fg="snow", cursor="mouse", relief="raised")
    img = ImageTk.PhotoImage(Image.open("stats1.png"))
    b3 = Button(root, image=img, cursor="mouse", relief="raised", padx=10, pady=20)
    b3.bind("<Button-1>", stats)
    b3.image=img
    b3.grid(row=2, column=0)
    img = ImageTk.PhotoImage(Image.open("exit1.png"))
    #b4 = Button(root, text="EXIT CLIENT", bg="dark violet", fg="snow", cursor="mouse", relief="raised", command=turn_back)
    b4 = Button(root, image=img, cursor="mouse", relief="raised", padx=10, pady=20)
    b4.bind("<Button-1>", seen)
    b4.image=img
    b4.grid(row=3, column=0)
    


def login():
    root = Tk()
    root.title("Client Login")

    l1 = Label(root, text="NAME", fg="goldenrod", font ="Purisa")
    l1.grid(row=0, stick=W)
    l2 = Label(root, text="PASS", fg="goldenrod", font ="Purisa")
    l2.grid(row=1, stick=W, columnspan=1)
    global e1
    global e2
    e1 = Entry(root)
    e1.insert(0, 'Username...')
    e1.bind('<FocusIn>', on_entry_click1)
    e1.bind('<FocusOut>', on_focusout1)
    e1.config(fg = 'grey')
    e1.grid(row=0, column=1)
    e1.focus_set()
    
    e2 = Entry(root)
    e2.insert(0, 'Password...')
    e2.bind('<FocusIn>', on_entry_click2)
    e2.bind('<FocusOut>', on_focusout2)
    e2.config(fg = 'grey')
    e2.grid(row=1, column=1)
    e2.focus_set()

    def login2(self):
        global client_id
        global client_pass
        client_id = e1.get()
        client_pass = e2.get()
        flag = 1
        for file in os.listdir("clients"):
            if file == client_id+'_'+client_pass+'.txt':
                l3=Label(root, text="Welcome "+client_id, fg="cyan", font ="Purisa")
                l3.grid(row=3)
                flag=0
                root.destroy()
                choice()
                
        if flag:
            l4=Label(root, text="Invalid credentials!", fg="gray1", font ="Purisa")
            l4.grid(row=3)

    b1 = Button(root, text="LOGIN", bg="RoyalBlue1", fg="red", cursor="man", relief="groove")
    b1.bind('<Button-1>', login2)
    root.bind('<Return>', login2)
    b1.grid(columnspan=2)

    logo=Label(root, text="DN", font=("Symbol", 20), fg="red4", borderwidth=5, relief="groove")
    logo.grid(row=0, column=2, rowspan=2, columnspan=2, ipadx=5, ipady=5, padx=13, pady=13)

    root.mainloop()

def start():
    login()

if __name__ == "__main__":
    start()
