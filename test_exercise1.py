import pytest
from exercise_1 import number_check


def test_3():
    n = 3
    assert "fizz" == number_check(n)


def test_5():
    number_count = 5
    assert "buzz" == number_check(number_count)


def test_3_and_5():
    number_count = 15
    assert "fizz buzz" == number_check(number_count)
