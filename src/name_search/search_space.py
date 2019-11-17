# -*- coding: utf-8 -*-
"""
replace spaces in file and directory names with underscores
a TDD approach
"""

__version__ = "0.0.1"

import os


def foo2bar(dirpath, filename):
    path = os.path.join(dirpath, filename)
    with open(path, 'rb') as input:
        data = input.read()
    data = data.replace(b'foo', b'bar')
    with open(path, 'wb') as output:
        output.write(data)

def search_for_spaces():
    file_list = ['foo foo.txt']
    return file_list
