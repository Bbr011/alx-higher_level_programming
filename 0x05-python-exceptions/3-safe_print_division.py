#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        n = x / y
        return (n)
    except ZeroDivisionError:
        return (None)
    finally:
        print("Inside result: {}".format(n))
