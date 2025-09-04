import pytest
from app import add, divide

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (9, 3, 3),
    (6, 2, 3),
])
def test_division(a, b, expected):
    assert divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
