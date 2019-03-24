#! /usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
import os
import datetime as dt
import tkinter.messagebox
import list_extractor as liex
import time
from collections import Counter
import d_netflix_gui

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
    root = Tk()
    root.title("SERVER MAIN-MENU")


    def turn_back():
        root.destroy()
        d_netflix_gui.greet()
    
    def client_stats(client_id, client_pass):
        root3=Tk()
        root3.title("CLIENT STATS")
        l9=Label(root3, text="Client id: "+client_id+"\t\t"+"Client Password: "+client_pass+'\t\t'+"DateTime: "+time.ctime()+"\n", fg="gray0")
        l9.grid(row=0)
        f = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
        ff = f.readlines()
        f.close()
        l10 = Label(root3, text="Total "+str(len(ff))+" films have been watched so far.\n"+client_id+" favourate films:\n", fg = "green2")
        l10.grid(row=1)
        text = [x.split('\t') for x in ff]
        frequent = [x[1].replace('\n', '') for x in text]
        counter = Counter(frequent).most_common(3)
        for x in counter:
            lt = Label(root3, text=x[0]+"\n", fg="blue")
            lt.grid()
        def close_all_(self):
                root3.destroy()
        bca = Button(root3, text="CLOSE", fg="red", bg="gray5")
        bca.bind('<Button-1>', close_all_)
        bca.grid()
        
    def client_info(self):
        files = []
        for file in os.listdir("clients/"):
            if file.endswith(".txt"):
                files.append(file)
        for file in files:
            client = file.split("_")
            client_id = client[0]
            client_pass = client[1].split('.txt')[0]
            client_stats(client_id, client_pass)

    def available_movies(self):
        global root5
        global root6
        global root7
        try:
            if root6:
                root6.destroy()
        except:
            try:
                if root5:
                    root5.destroy()
            except:
                pass
        root7=Tk()
        root7.title("AVAILABLE MOVIES")
        file = open('dsap_92det.txt', "r")
        file_text = file.readlines()
        file.close()
        file_r_text = liex.cleaner(file_text)
        la1=Label(root7, text="Following "+str(len(file_r_text))+" movies we have -->", fg="yellow")
        la1.grid(row=0)
        count = 1
        count2 = 0
        for line in file_r_text:
            la2 = Label(root7, text=str(count)+'.)\t'+line[1]+'\t\t'+'Genre: '+line[2], anchor=W)
            count += 1
            la2.grid(row=1+count2)
            count2+=1
        root.mainloop()


    def watch_frequency(self):
        global root5
        global root6
        global root7
        try:
            if root5:
                root5.destroy()
        except:
            try:
                if root7:
                    root7.destroy()
            except:
                pass
        root6 = Tk()
        root6.title("WATCH FREQUENCY")
        file = open("collective.txt", "r")
        file_text = file.readlines()
        file.close()
        text = [x.split('\t') for x in file_text]
        frequent = [x[1].replace('\n', '') for x in text]
        la1 = Label(root6, text="Frequency\t Film:::\n", fg="yellow")
        la1.grid(row=0)
        count=0
        for x in Counter(frequent):
            la2 = Label(root6, text=str(Counter(frequent)[x])+'\t\t'+x, fg="blue", anchor=W)
            la2.grid(row=1+count)
            count+=1
        root6.mainloop()
        
    def thorough_description(self):
        global root5
        global root6
        global root7
        try:
            if root6:
                root6.destroy()
        except:
            try:
                if root7:
                    root7.destroy()
            except:
                pass
        root5=Tk()
        root5.title("COMPLETE DESCRIPTION")
        f = open("collective.txt", "r")
        ff = f.readlines()
        f.close()
        la1 = Label(root5, text="Total "+str(len(ff))+" films have been played so far.\n", fg="gold")
        la1.grid(row=0)
        text = [x.split('\t') for x in ff]
        frequent = [x[1].replace('\n', '') for x in text]
        counter = Counter(frequent).most_common(5)
        la2=Label(root5, text="5 Most popular films:", fg="lawn green")
        la2.grid(row=1)
        count = 0
        for x in counter:
            la3= Label(root5, text=x[0], fg="blue")
            la3.grid(row=2+count)
            count+=1
            
        root5.mainloop()

    def movie_stats(self):
        root4=Tk()
        bu1 = Button(root4, text="AVAILABLE MOVIES", fg="blue", bg="gold", relief="groove", width=20)
        bu2 = Button(root4, text="WATCH FREQUENCY", fg="blue", bg="gold", relief="groove", width=20)
        bu3 = Button(root4, text="COMPLETE DESCRIPTION", fg="blue", bg="gold", relief="groove", width=20)
        bu1.bind("<Button-1>", available_movies)
        bu1.grid(row=0, column=0)
        bu2.bind("<Button-1>", watch_frequency)
        bu2.grid(row=0, column=1)
        bu3.bind("<Button-1>", thorough_description)
        bu3.grid(row=0, column=2)
        root4.mainloop()

    def requests():
        root2 = Tk()
        root2.title("STATS WINDOW")
        b7 = Button(root2, text="CLIENT STATS", fg="blue", bg="OliveDrab1", relief="groove", width=15, cursor="sizing")
        b7.bind("<Button-1>", client_info)
        b7.grid(row=0, column=0)
        b8 = Button(root2, text="MOVIE STATS", fg="blue", bg="OliveDrab1", relief="groove", width=15, cursor="sizing")
        b8.bind("<Button-1>", movie_stats)
        b8.grid(row=0, column=1)
        root2.mainloop()
    
    def remove():
        def remove_code(self):
            title = e6.get()
            answer=tkinter.messagebox.askquestion("Admin Access", "Delete "+title)
            if answer=="yes":
                database = open("dsap_92det.txt", "r")
                lines = database.readlines()
                o_lines = lines # lines is not a nested list so no trouble
                database.close()
    
                database = open('dsap_92det.txt', "w")
                lines = liex.cleaner(lines)
                for x in range(len(lines)):
                    if title!=lines[x][1]:
                        database.write(str(o_lines[x]))
                    else:
                        tkinter.messagebox.showinfo("Deleted Successfuly", title+" is deleted successfully")
                        break
                else:
                    tkinter.messagebox.showinfo("Film Not Present", title+" is not present")
                database.close()
            root2.destroy()

        root2=Tk()
        root2.title("Remove a Movie")
        l7 = Label(root2, text = "Give Title of Movie to be Deleted", font="Aerial", fg="orange red")
        l7.grid(row=0)

        e6 = Entry(root2, width=50)
        e6.grid(row=1)
        e6.focus_set()

        b6 = Button(root2, text="Delete", relief="groove")
        b6.bind("<Button-1>", remove_code)
        b6.grid(row=2, columnspan=2)

        root2.bind("<Return>", remove_code)
        

    
    def upload():
        def upload_code(self):
            database = open("dsap_92det.txt", "a+")
            td = dt.datetime.now()
            link = e3.get()
            title = e4.get()
            genre = e5.get()
            if link=="":
                l6 = Label(root2, text="You forgot Link!", fg="red2", font ="Purisa")
                l6.grid(row=4, column=1, columnspan=2)
            elif title=="":
                l6 = Label(root2, text="You forgot Title!", fg="red2", font ="Purisa")
                l6.grid(row=4, column=1, columnspan=2)
            elif genre=="":
                l6 = Label(root2, text="You forgot Genre!", fg="red2", font ="Purisa")
                l6.grid(row=4, column=1, columnspan=2)
            else:
                database.write(str([link, title, genre, td.year, td.month, td.day, td.hour, td.minute, td.second])+'\n')
                database.close()
                l6 = Label(root2, text="Movie has been uploaded successfully.", fg="hot pink", font ="Purisa")
                l6.grid(row=4, column=1, columnspan=2)
                root2.destroy()

            
        root2=Tk()
        root2.title("UPLOAD MOVIES")
        l3 = Label(root2, text="LINK", fg="SeaGreen1", font ="Purisa")
        l3.grid(row=0, stick=W)
        l4 = Label(root2, text="TITLE", fg="SeaGreen1", font ="Purisa")
        l4.grid(row=1, stick=W)
        l5 = Label(root2, text="GENRE", fg="SeaGreen1", font ="Purisa")
        l5.grid(row=2, stick=W)

        e3 = Entry(root2, width=50)
        e3.grid(row=0, column=1, columnspan=2)
        e3.focus_set()

        e4 = Entry(root2, width=50)
        e4.grid(row=1, column=1, columnspan=2)
        e4.focus_set()
        
        e5 = Entry(root2, width=50)
        e5.grid(row=2, column=1, columnspan=2)
        e5.focus_set()

        b5 = Button(root2, text="UPLOAD", bg="blue2", fg="red", cursor="man", relief="raised", width=50)
        b5.bind('<Button-1>', upload_code)
        root2.bind('<Return>', upload_code)
        b5.grid(row=3, column=1)
        
        root.mainloop()
        
        
    b1 = Button(root, text="UPLOAD", bg="dark violet", fg="snow", cursor="mouse", relief="raised", command=upload)
    b1.grid(row=0, column=0)
    b2 = Button(root, text="REMOVE", bg="dark violet", fg="snow", cursor="mouse", relief="raised", command=remove)
    b2.grid(row=0, column=1)
    b3 = Button(root, text="STATS", bg="dark violet", fg="snow", cursor="mouse", relief="raised", command=requests)
    b3.grid(row=0, column=2)
    b4 = Button(root, text="EXIT SERVER", bg="dark violet", fg="snow", cursor="mouse", relief="raised", command=turn_back)
    b4.grid(row=0, column=3)

    
    root.mainloop()

def login():
    root = Tk()
    root.title("Server Login")

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
        server_id = e1.get()
        server_pass = e2.get()
        flag = 1
        for file in os.listdir():
            if file == server_id+'_'+server_pass+'.txt':
                l3=Label(root, text="Database access granted.", fg="cyan", font ="Purisa")
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
