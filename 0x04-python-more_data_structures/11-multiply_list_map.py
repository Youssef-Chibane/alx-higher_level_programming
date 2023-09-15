#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    result = [element * number for element in new_list]
    return result
