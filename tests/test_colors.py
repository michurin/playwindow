# coding: U8


import pytest

from playwindow.color import from_rgb, from_hsl, from_cmy


@pytest.mark.parametrize('r,g,b,res', (
    (0, 0, 0, '#000000'),
    (50, 0, 0, '#7f0000'),
    (0, 50, 0, '#007f00'),
    (0, 0, 50, '#00007f'),
    (100, -1, 101, '#ff00ff')
))
def test_rgb(r, g, b, res):
    assert from_rgb(r, g, b) == res


@pytest.mark.parametrize('h,s,l,res', (
    # l = 0
    (0, 0, 0, '#000000'),
    (0, 100, 0, '#000000'),
    # s
    (0, 50, 100, '#ff7f7f'),
    (0, 100, 100, '#ff0000'),
    (0, 100, 50, '#7f0000'),
    # h
    (0, 100, 100, '#ff0000'),
    (60, 100, 100, '#ffff00'),
    (120, 100, 100, '#00ff00'),
    (180, 100, 100, '#00ffff'),
    (240, 100, 100, '#0000ff'),
    (300, 100, 100, '#ff00ff'),
    # out of range
    (-360, 101, 101, '#ff0000'),
    (720, 101, 101, '#ff0000'),
    (0, -1, -1, '#000000')
))
def test_hsl(h, s, l, res):
    assert from_hsl(h=h, s=s, l=l) == res


@pytest.mark.parametrize('c,m,y,res', (
    (0, 0, 0, '#ffffff'),
    (100, 100, 100, '#000000'),
    (100, 0, 0, '#00ffff'),
    (0, 100, 0, '#ff00ff'),
    (0, 0, 100, '#ffff00'),
    (50, 0, 0, '#7fffff'),
))
def test_cmy(c, m, y, res):
    assert from_cmy(c=c, m=m, y=y) == res
