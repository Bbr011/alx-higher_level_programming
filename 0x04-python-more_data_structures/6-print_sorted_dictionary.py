#!/usr/bin/python3i
def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())

    for key in sorted_keys:
        print(f"{key}: {a_dictionary[key]}")
