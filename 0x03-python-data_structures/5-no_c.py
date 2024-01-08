#!/usr/bin/env python3
def no_c(my_string):
    a = len(my_string)
    for i in a:
        if my_string[i] != "c":
            print(f"{my_string[i]}")
