#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    tempo_list = my_list[:]
    if 0 <= idx < len(my_list):
        tempo_list[idx] = element
        return (tempo_list)
    return (my_list)
