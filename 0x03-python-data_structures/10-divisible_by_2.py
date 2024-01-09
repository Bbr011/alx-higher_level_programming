#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = my_list[:]
    for i, j in enumerate(my_list):
        if i % 2 == 0:
            newlist[j] = True
        else:
            newlist[j] = False
    return (newlist)
