#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    nlist = my_list[:]
    for i, j in enumerate(my_list):
        if i % 2 == 0:
            nlist[j] = True
        else:
            nlist[j] = False
    return (nlist)
