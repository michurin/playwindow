#!/usr/bin/python3
# coding: U8


import random

from playwindow import window, oval, from_hsl, move, wait_for_click, overlapping, delete, find_all


def main():
    window(400, 400, background='#000')
    while True:
        for _ in range(30):
            h = 360 * random.random()
            o = oval(
                0, 0, 100, 100,
                fill=from_hsl(h=h, s=100, l=70),
                outline=from_hsl(h=h, s=100, l=100),
                width=1
            )
            x = random.random() * 300
            y = random.random() * 300
            move(o, x, y)
        while True:
            e = wait_for_click()
            oo = overlapping(e.x-1, e.y-1, e.x+1, e.y+1)
            if len(oo) > 0:
                delete(*oo)
            if len(find_all()) == 0:
                break


if __name__ == '__main__':
    main()
