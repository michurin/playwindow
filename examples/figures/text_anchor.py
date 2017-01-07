#!/usr/bin/python3
# coding: U8


from playwindow import window, oval, text

window(width=600, height=200, background='#000')

for x, y, anchor in (
        (100,  50, 'nw'), (300,  50,      'n'), (500,  50, 'ne'),
        (100, 100,  'w'), (300, 100, 'center'), (500, 100, 'e'),
        (100, 150, 'sw'), (300, 150,      's'), (500, 150, 'se'),
    ):
    txt = '[anchor=%r]' % anchor
    oval(x - 2, y - 2, x + 2, y + 2, fill='#f00', width=0)
    text(x, y, text=txt, anchor=anchor, font={'size': 12}, fill='#fff')
