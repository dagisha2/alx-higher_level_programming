#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        str = "{:d}"
        print(str.format(i))
    return my_list
