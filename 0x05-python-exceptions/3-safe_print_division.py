#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        n = x / y
    except ZeroDivisionError:
        n = None
    finally:
        print("Inside result: {}".format(n))
    return (n)
