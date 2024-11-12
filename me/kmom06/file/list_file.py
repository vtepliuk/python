#!/usr/bin/env python3
"""
Example of how to read the content of a file into a list
"""

filename = "items.txt"

with open(filename) as filehandle:
    items_as_list = filehandle.readlines()
print(items_as_list)


items_as_list.append("cup")
print(items_as_list)

list_as_str = ",".join(items_as_list)
print(list_as_str)

with open(filename, "w") as filehandle:
    filehandle.write(list_as_str)
