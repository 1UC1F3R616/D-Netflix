#! /usr/bin/env python
# -*- coding: utf-8 -*-

import server_file
import client_file

def greet():
    print("Hi! This is D-Netflix, A simple application based on Stack and queue.")
    print("New user may refer to User_guide firstly.\n\n")

def side():
    print("Are you a Client or Server?")
    print("Press 'C' or 'c' for client and hit enter.")
    print("Press 'S' or 's' for server and hit enter.")
    side_var = input()
    print()
    if side_var in ('S', 's'):
        server_file.start()
        # Server will be started
    elif side_var in ('C', 'c'):
        client_file.start()
        # Client will be started
    else:
        print("Invalid choice\n")
        side()
