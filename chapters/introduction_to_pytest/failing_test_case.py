import pytest


# test function
def f():
    return 3


# failed test case
def test_one_plus_two():
    a = 1
    b = 2
    c = 0

    assert a + b == c


# failed test case based on function return
def test_function_f():
    assert f() == 4
