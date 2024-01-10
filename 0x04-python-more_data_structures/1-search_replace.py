#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for i in range(len(my_list)):
        new_list(my_list.index(search)) = replace
        return (new_list)
    return (my_list)
