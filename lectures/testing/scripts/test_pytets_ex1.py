import pytest
from ex1 import Calc


@pytest.mark.parametrize(
    ("a", "b", "c"),
    [
        (1, 1, 2),
        (2, 1, 5),
        (2, 2, 4),
    ]
)
def test_sum(a, b, c):
    assert Calc.sum(a, b) == c


@pytest.fixture
def set_up_mul():
    pass
