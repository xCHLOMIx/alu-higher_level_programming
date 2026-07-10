#!/usr/bin/python3
def safe_print_division(a, b):
    r = None
    try:
        r = a / b
    except ZeroDivisionError:
        pass
    finally:
        print("{}".format(r))
        return r
