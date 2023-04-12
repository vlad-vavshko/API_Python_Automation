import pytest

# Multiplication test ideas
# two positive integers
# identity: multiplying any number by 1
# zero: multiplying any number by 0
# positive by a negative
# negative by a negative
# multiplying floats

multiplication = [
    (2, 3, 6),
    (1, 99, 99),
    (0, 99, 0),
    (3, -4, -12),
    (-5, -5, 25),
    (2.5, 6.7, 16.75),
]


@pytest.mark.parametrize("a, b, result", multiplication)
def test_multiplication(a, b, result):
    assert a * b == result


division = [
    (10, 0, False),  # divide by zero
    (6, 3, 2),  # bigger / smaller
    (1, 2, 0.5),  # smaller / bigger
    (5, 5, 1),  # number by itself
    (52.4, 2.5, 20.96),  # divide floats
    (10, -2, -5),  # divide positive by negative
    (100, 1, 100),  # divide by one
]


@pytest.mark.parametrize("a, b, result", division)
def test_division(a, b, result):
    if b != 0:
        assert a / b == result
    else:
        with pytest.raises(ZeroDivisionError):
            assert a / b == result
