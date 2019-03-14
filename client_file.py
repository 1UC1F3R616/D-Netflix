#! /usr/bin/env python
# -*- coding: utf-8 -*-

import webbrowser
#import os
import server_file
import start_file
import time
import list_extractor as liex
from collections import Counter

global server_id
global server_pass
server_id = "dsap"
server_pass = "92det"
global collective
collective = "collective.txt"

def login():
    global client_id
    global client_pass
    client_id = input("Give your id: ")
    client_pass = input("Give your pass: ")

    try:
        client_access = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
        print("Welcome "+client_id+".\n")
        client_access.close()
        return True
    except:
        return False

def signup():
    global client_id
    global client_pass
    client_id = input("Give your id: ")
    client_pass = input("Create a password for id: ")
    try:
        exsist = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
        if exsist:
            print("Sorry, this username is already registered.")
            print()
            exsist.close()
            signup()
        
    except:
        client_sign = open("clients/"+client_id+'_'+client_pass+'.txt', "w")
        client_sign.close()
        print("Your database has been created successfully.")
        print()

def search():
    m_name = input('Give name of film: ')
    file = open(server_id+'_'+server_pass+'.txt', "r")
    file_text = file.readlines()
    file.close()
    file_r_text = liex.cleaner(file_text)
    for x in file_r_text:
        if x[1]==m_name:
            print("Yes, we have "+m_name)
            break
    else:
        print("Sorry, We don't have this film.")
    print()

def watch():
    title = input("Give title of movie to watch: ")

    file = open(server_id+'_'+server_pass+'.txt', "r")
    file_text = file.readlines()
    file.close()
    file_r_text = liex.cleaner(file_text)
    for line in file_r_text:
        if line[1]==title:
            print("Now watching "+title+' at '+time.ctime())
            file = open("clients/"+client_id+'_'+client_pass+'.txt', "a+")
            file.write(time.ctime()+'\t '+title+'\n')
            collect = open(collective, "a+")
            collect.write(time.ctime()+'\t '+title+'\n')
            collect.close()
            file.close()
            webbrowser.open(line[0])
            print()
            break
    else:
        print("This film is currently unavilable.\n")

def recommend(): # queue-> When server see it, it falls in first in first out
    file = open("recommend.txt", "a+")
    file.write(input("Suggest the film name: ")+'\n')
    file.close()
    print("We will act in shortly!\n")

def history(): # first in last out
    file = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
    file_text = file.readlines()
    file.close()
    file_text.reverse()
    print("DateTime                 \tFilm:::")
    for line in file_text:
        print(line, end='')
    print()

def available_movies(): #first in first out
    file = open(server_id+'_'+server_pass+'.txt', "r")
    file_text = file.readlines()
    file.close()
    file_r_text = liex.cleaner(file_text)
    print("Following "+str(len(file_r_text))+" movies we have -->")
    count = 1
    for line in file_r_text:
        print(str(count)+'.)\t'+line[1]+'\t'+'Genre: '+line[2])
        count += 1
    print()
    

def watch_frequency():
    file = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
    file_text = file.readlines()
    file.close()
    text = [x.split('\t') for x in file_text]
    frequent = [x[1].replace('\n', '') for x in text]
    print("Frequency\t Film:::")
    for x in Counter(frequent):
        print(str(Counter(frequent)[x])+'\t\t'+x)
    print()

def thorough_description(c_id="client_id", c_pass="client_pass"):
    global client_id
    global client_pass
    if __name__ == "__main__":
        pass
    else:
        client_id = c_id
        client_pass = c_pass
    print()
    print("Client id: "+client_id+"\t\t"+"Client Password: "+client_pass+'\t\t'+"DateTime: "+time.ctime())
    print()
    f = open("clients/"+client_id+'_'+client_pass+'.txt', "r")
    ff = f.readlines()
    f.close()
    print("Total "+str(len(ff))+" films have been watched so far.")
    text = [x.split('\t') for x in ff]
    frequent = [x[1].replace('\n', '') for x in text]
    counter = Counter(frequent).most_common(3)
    print()
    print(client_id+" favourate films:")
    for x in counter:
        print(x[0])
    print("\n")

def movie_stats():
    print("Key:\tOperation:")
    print("1\tTo see available films.")
    print("2\tTo see movies watch frequency.") # Will develope in last
    print("3\tTo see a thorough description.") # Will add once I add date, genre etc in database.
    print("4\tTo search for a film.")
    choice = input()
    print()
    if choice == '1' :
        available_movies()
    elif choice == '2' :
        watch_frequency()
    elif choice == '3':
        thorough_description()
    elif choice== '4':
        search()
    else:
        print("Invalid choice!")

def choice():
    choice = input("Enter your choice: ")
    print()
    while choice not in ('1', '2', '3', '4', '5', '6'):
        print("Invalid choice.")
        print() #formating is done
        choice = input("Enter your choice again: ")
        if choice in ('1', '2', '3', '4', '5', '6'): # some lazy issue I had here, so this.
            print()
            break
        
    if choice == '1':
        watch()
    elif choice == '2':
        movie_stats()
    elif choice == '3':
        recommend()
    elif choice == '4':
        history()
    elif choice == '5':
        print("Closing database")
        print("Exiting server.")
        print()
        start_file.side()
    elif choice == '6':
        print("Exiting D-Netflix")
        exit()

global count
count = 0
def start():
    global count
    count += 1
    print("New users press 'yes' or 'YES' or '1'")
    print("Existed users may press Enter.")
    user_type = input()
    if user_type in ('yes', 'YES', '1'):
        signup()
        login_stat = True
    else:
        login_stat = login()

    if login_stat:
        print("Key:\tOperation:")
        print("1\tTo Watch a film.")
        print("2\tTo See film stats.")
        print("3\tRecommend a film.")
        print("4\tTo view your watch history") #stack
        print("5\tTo exit the client.")
        print("6\tTo exit D-Netflix.")
        print()
    else:
        print("Invalid login credentials, please try again!\n")
        if count%2==0:
            change = input("Do you want to get back? Press 1 or 'yes', 'YES' if yes. ")
            print()
            if change in ('1', 'yes', 'YES'):
                print()
                start_file.side()
        start()

    while True:
        choice()


if __name__ == "__main__":
    start()
