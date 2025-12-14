import math

import pytest

from src import calculator


def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0


def test_subtract():
    assert calculator.subtract(10, 4) == 6
    assert calculator.subtract(0, 5) == -5


def test_multiply():
    assert calculator.multiply(7, 6) == 42
    assert calculator.multiply(-3, 5) == -15


def test_divide():
    assert calculator.divide(9, 3) == 3
    assert calculator.divide(-8, 2) == -4


def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (0.1, 0.2, 0.3),
        (1.5, 2.5, 4.0),
        (math.pi, math.e, math.pi + math.e),
    ],
)
def test_add_floats(a, b, expected):
    assert calculator.add(a, b) == pytest.approx(expected)
