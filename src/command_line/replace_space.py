#!/usr/bin/env python3
"""
Change spaces with underscore in directories and files
"""

import sys
import os.path


def command_line_arguments():
    return sys.argv


if __name__ == '__main__':
    arguments = command_line_arguments()
    number_of_arguments = len(arguments)
    filename = arguments[0]
    print(f"\nCommand line program {os.path.split(filename)[1]} started\n")
    print(f"Number of arguments = {number_of_arguments}\n")
    for a in arguments:
        print(f"{a}")
