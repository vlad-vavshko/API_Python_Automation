# Unit testing of classes

import pytest
from stuff_for_testing_classes.accum import Accumulator


# Test

def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0


def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly():
    accum = Accumulator()
    with pytest.raises(AttributeError, match="roperty 'count' of 'Accumulator' object has no setter") as err_info:
        accum.count = 10
