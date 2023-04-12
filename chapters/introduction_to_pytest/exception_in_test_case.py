import pytest


# wrong statement -> DID NOT RAISE <class 'ZeroDivisionError'>
def test_divide_by_num():
    with pytest.raises(ZeroDivisionError) as e:
        assert 6 / 2 == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert "division by zero" in str(e.value)


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)
