#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for elemnt in range(len(my_list)):
        if new_list[elemnt] == search:
            new_list[elemnt] = replace
    return new_list
