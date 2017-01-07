# coding: U8


import pytest

from tests.module import * # pylint: disable=wildcard-import,unused-wildcard-import


def test_function():
    assert x(1) == 1


def test_class():
    assert X(1).get_x() == 1


def test_private():
    with pytest.raises(NameError):
        y()
