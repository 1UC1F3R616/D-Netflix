#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""Firstly readlines from file and store it in a list/tuple simply pass the list/tuple to the below cleaner function and it returns clean_data, which is a nested list of your data."""
# Your data should be like below only, or else modification maybe needed.
# data = ["['https://www.youtube.com/watch?v=I0TinhhUwKQ', 'kush']\n", "['https://www.youtube.com/watch?v=I0TinhhUwKQ', 'unknown']\n"]

def cleaner(data):
    clean1 = []
    clean2 = []
    clean3 = []
    for x in data:
        clean1.append(x[1:len(x)-2])
    for x in clean1:
        clean2.append(x.split(', '))
    for x in clean2:
        clean = [x[0][1:len(x[0])-1], x[1][1:len(x[1])-1], x[2][1:len(x[2])-1]]
        clean3.append(clean)
    return clean3

if __name__ == "__main__":
    file_name = input("Give file name to be parsed, with proper format: ")
    file_open = open(file_name, "r")
    data = file_open.readlines()
    clean_data = cleaner(data)
    print(clean_data)
