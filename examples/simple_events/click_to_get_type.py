#!/usr/bin/python3
# coding: U8


import random

from playwindow import window, text, oval, rectangle, wait_for_click, overlapping, raise_item, configure, from_hsl, item_type


def main():
    window(300, 200, background='#000')
    o = text(150, 20, 'click to get type...')
    oval(10, 90, 140, 190, fill='#888')
    rectangle(160, 90, 290, 190, fill='#888')
    while True:
        e = wait_for_click()
        targets = overlapping(e.x-1, e.y-1, e.x+1, e.y+1)
        if len(targets) > 0:
            target = targets[-1]
            c = from_hsl(h=random.random() * 360, s=100, l=100)
            raise_item(target)
            configure(o, text=item_type(target), fill=c)
            configure(target, fill=c)


if __name__ == '__main__':
    main()
