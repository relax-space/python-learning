import pytest

pytestmark = pytest.mark.parametrize('test_input, expected', [(1, 2), (3, 4)])


def test_module(test_input, expected):
    assert test_input + 1 == expected
