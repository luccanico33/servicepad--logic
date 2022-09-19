import pytest
from exercise_3 import words_counter


def test_words_counter():
    text_test = "Hello, Hello? hello!!!  this is a white pen, this pen is white and this white pen is my favourite "

    counter_test = {
        "HELLO": 3,
        "THIS": 3,
        "WHITE": 3,
        "PEN": 3,
        "IS": 3,
        "A": 1,
        "AND": 1,
        "MY": 1,
        "FAVOURITE": 1,
    }

    assert counter_test == words_counter(text_test.upper())
