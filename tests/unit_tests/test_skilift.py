from skilift import Lift, Line

import pytest


@pytest.mark.bench_size(6)
def test_bench6(BenchN, line5):
    lift = Lift(10, BenchN)
    res = lift.one_bench(line5)
    assert res == {'loaded': 5, 'num_benches': 1, 'unloaded': 0}


@pytest.mark.line_size(6)
def test_line6(line_n):
    res = line_n.take(6)
    assert res == 6


def test_line_take(line5):
    #line = Line(5)
    res = line5.take(7)
    assert res == 5
    assert line5.num_people == 0


def test_lift_one_bench(line5, quad10):
    #line = Line(5)
    #lift = Lift(10, Quad)
    res = quad10.one_bench(line5)
    assert res == {'loaded': 4, 'num_benches': 1, 'unloaded': 0}


@pytest.mark.parametrize('size',
            [[],None,'10'])
def test_line_bad(size):
    line = Line(size)
    with pytest.raises(TypeError):
        res = line.take(1)


# @pytest.mark.parametrize('line_size, take_count, num_people',
#                          [(0,5,0),
#                           (5, 2, 3),
#                          (10, 0, 10)])
@pytest.mark.parametrize('line_size, take_count, num_people', [(0, 5, 0), (5, 2, 3), (10, 0, 10)])
def test_line_sizes(line_size,
                    take_count,
                    num_people):
    line = Line(line_size)
    res = line.take(take_count)
    assert line.num_people == num_people


def test_half_take(monkeypatch):
    def half_take(self, amount):
        amount = int(amount/2)
        if amount > self.num_people:
            amount = self.num_people
        self.num_people -= amount
        return amount
    monkeypatch.setattr(Line, 'take', half_take)
    line = Line(10)
    res = line.take(5)
    assert res == 2

    
