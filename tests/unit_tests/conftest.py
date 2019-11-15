from skilift import _Bench, Lift, Line, Quad


import pytest


@pytest.fixture
def line_n(request):
    size = request.node.get_closest_marker(
        'line_size').args[0]
    line = Line(size)
    return line


@pytest.fixture
def line5():
    line = Line(5)
    return line

@pytest.fixture
def quad10():
    lift = Lift(10, Quad)
    return lift


@pytest.fixture
def BenchN(request):
    size_ = request.node.get_closest_marker(
        'bench_size').args[0]
    class BSize(_Bench):
        size = size_
    return BSize

