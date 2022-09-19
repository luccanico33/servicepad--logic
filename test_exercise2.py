import pytest
from exercise_2 import counter_fibo


def test_fibonacci():
    number_test = 10
    assert 89 == counter_fibo(number_test)


def test_fibonacci_error():
    number_test = -1
    assert "unable to get a value" in counter_fibo(number_test)
