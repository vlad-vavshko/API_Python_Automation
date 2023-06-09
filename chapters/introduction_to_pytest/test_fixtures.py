# Fixtures are used to set up the precondition for tests

import pytest
from stuff_for_testing_classes.accum import Accumulator


# Fixtures
@pytest.fixture
def accum():
    return Accumulator()

# Test

def test_accumulator_init(accum):
    assert accum.count == 0


def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1


def test_accumulator_add_three(accum):
    accum.add(3)
    assert accum.count == 3


def test_accumulator_add_twice(accum):
    accum.add()
    accum.add()
    assert accum.count == 2


def test_accumulator_cannot_set_count_directly(accum):
    with pytest.raises(AttributeError, match="roperty 'count' of 'Accumulator' object has no setter") as err_info:
        accum.count = 10
