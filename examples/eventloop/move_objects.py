#!/usr/bin/python3
# coding: U8


import random

from playwindow import window, window_cursor, oval, wait, overlapping, raise_item, move, EventMouseButtonPress, EventMouseButtonRelease, EventMouseMove


def main():
    window(400, 400, background='#000')
    window_cursor('hand1')
    oval(0, 0, 100, 100, fill='#050', outline='#0f0', width=2)
    oval(0, 0, 100, 100, fill='#050', outline='#0f0', width=2)
    oval(0, 0, 100, 100, fill='#050', outline='#0f0', width=2)
    px = None
    py = None
    o = None
    while True:
        e = wait()
        if type(e) is EventMouseButtonPress:
            px = e.x
            py = e.y
            oo = overlapping(px-1, py-1, px+1, py+1)
            if len(oo) > 0:
                o = oo[-1]
                raise_item(o)
                window_cursor('fleur')
        if type(e) is EventMouseButtonRelease:
            o = None
            window_cursor('hand1')
        if type(e) is EventMouseMove and not o is None:
            move(o, e.x - px, e.y - py)
            px = e.x
            py = e.y


if __name__ == '__main__':
    main()
