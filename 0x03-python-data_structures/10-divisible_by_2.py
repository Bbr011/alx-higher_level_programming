#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for i, j in enumerate(my_list):
        if i % 2 == 0:
            new_list[j] = true
        else:
            new_list[j] = false
    return (new_list)
