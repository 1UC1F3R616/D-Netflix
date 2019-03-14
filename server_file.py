#! /usr/bin/env python
# -*- coding: utf-8 -*-

import start_file
import list_extractor as liex
import datetime as dt
import client_file
import os
from collections import Counter

global collective
collective = "collective.txt"

def login():
    global server_id
    global server_pass
    server_id = input("Give server id: ")
    server_pass = input("Give server pass: ")

    try:
        database = open(server_id+'_'+server_pass+'.txt', "r")
        print("Database access granted.\n")
        database.close()
        return True
    except:
        return False

def choice():
    choice = input("\nEnter your choice: ")
    print()
    while choice not in ('1', '2', '3', '4', '5'):
        print("Invalid choice.")
        print()
        choice = input("Enter your choice again: ")
        if choice in ('1', '2', '3', '4', '5'):
            print()
            break
    
    if choice == '1':
        upload()
    elif choice == '2':
        remove()
    elif choice == '3':
        requests()
    elif choice == '4':
        print("Closing database")
        #database.close()
        print("Exiting server.")
        print()
        # break from here and take to start again
        start_file.side()
    elif choice == '5':
        #database.close()
        print("Exiting D-Netflix")
        exit()

def upload():
    global server_id
    global server_pass
    link = input("Give Link of film: ")
    title = input("Give Title of film: ")
    genre = input("Give Genre of film: ")
    print("Movie has been uploaded successfully.")
    print()
    database = open(server_id+'_'+server_pass+'.txt', "a+")
    td = dt.datetime.now()
    database.write(str([link, title, genre, td.year, td.month, td.day, td.hour, td.minute, td.second])+'\n')
    database.close()

def remove():
    title = input("Give title of movie to be deleted: ")
    database = open(server_id+'_'+server_pass+'.txt', "r")
    lines = database.readlines()
    o_lines = lines # lines is not a nested list so no trouble
    database.close()
    
    database = open(server_id+'_'+server_pass+'.txt', "w")
    lines = liex.cleaner(lines)
    #print(lines)
    for x in range(len(lines)):
        #print(title, line[1])
        if title!=lines[x][1]:
            database.write(str(o_lines[x]))
        else:
            print(title+" is successfully removed.\n")
    database.close()

def client_info():
    files = []
    for file in os.listdir("clients/"):
        if file.endswith(".txt"):
            files.append(file)
    for file in files:
        client = file.split("_")
        client_id = client[0]
        client_pass = client[1].split('.txt')[0]
        client_file.thorough_description(client_id, client_pass)

def available_movies():
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
    file = open(collective, "r")
    file_text = file.readlines()
    file.close()
    text = [x.split('\t') for x in file_text]
    frequent = [x[1].replace('\n', '') for x in text]
    print("Frequency\t Film:::")
    for x in Counter(frequent):
        print(str(Counter(frequent)[x])+'\t\t'+x)
    print()

def thorough_description():
    f = open("collective.txt", "r")
    ff = f.readlines()
    f.close()
    print("Total "+str(len(ff))+" films have been played so far.")
    text = [x.split('\t') for x in ff]
    frequent = [x[1].replace('\n', '') for x in text]
    counter = Counter(frequent).most_common(5)
    print()
    print("5 Most popular films:")
    for x in counter:
        print(x[0])
    print("\n")

def requests():
        print("To get client info--> press 'CI' or 'ci' and hit enter.")
        print("To get Movie stats--> press 'MS' or 'ms' and hit enter.")
        choice = input()
        if choice in ('CI', 'ci'):
            client_info()
        elif choice in ('MS', 'ms'):
            movie_stats()
        else:
            print("Invalid choice!")
            print("Taking back to main server menu.")


def movie_stats():
    print("Key:\tOperation:")
    print("1\tTo see available movies.")
    print("2\tTo see movies watch frequency.") # Will develope in last
    print("3\tTo see a thorough description.") # Will add once I add date, gener etc in database.
    choice = input()
    if choice == '1' :
        available_movies() # queue-> first in first out
    elif choice == '2' :
        watch_frequency()
    elif choice == '3':
        thorough_description()
    else:
        print("Invalid choice!")

global count
count = 0
def start():
    global count
    login_stat = login()
    count += 1
    if login_stat:
        print("Key:\tOperation:")
        print("1\tTo upload a movie.")
        print("2\tTo remove a movie.")
        print("3\tTo make special requests.")
        print("4\tTo exit the server.")
        print("5\tTo exit D-Netflix.")
    else:
        print("Invalid login credentials, please try again!\n")
        if count%2==0:
            change = input("Do you want to get back? Press 1 or 'yes', 'YES' if yes. ")
            if change in ('1', 'yes', 'YES'):
                print()
                start_file.side()
        start()

    while True:
        choice()
    

if __name__ == "__main__":
    start()
