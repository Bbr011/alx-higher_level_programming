#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = len(my_list)
    for i in rang(a):
        print(f"{my_list[-i]}")
        i -= 1
