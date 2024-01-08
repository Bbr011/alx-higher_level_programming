#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tempo_list = my_list
    if 0 <= idx < len(my_list):
        my_list[idx] = element
        return (my_list)
    return (tempo_list)
