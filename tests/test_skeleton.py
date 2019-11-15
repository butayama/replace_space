# -*- coding: utf-8 -*-

import pytest
from replace_space.skeleton import fib

__author__ = "Buta Yama"
__copyright__ = "Buta Yama"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
