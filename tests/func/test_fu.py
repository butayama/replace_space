"""
Change spaces with underscore in directories and files
"""
import unittest
import pytest
from search_space import search_for_spaces


def test_search_for_spaces():
    assert search_for_spaces() == ['foo foo.txt']


class AnalyseDirectoryTest(unittest.TestCase):

    # In my home directory I start the program (P) with
    # $ python replace_space_unused.py -analyse /home/uwe/D_sdb2/Blender
    # P lists files and directories on the screen with spaces in their name.
    pass
    # At the end of the output a list is shown:
    # 3 directoris with spaces in their name found
    # 2 .xcf files with spaces in their name found
    # 10 .jpg files with with spaces in their name found
