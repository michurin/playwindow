#!/usr/bin/python3
# coding: U8


import math

from playwindow import window, oval, coords, configure, sleep, from_rgb, from_hsl


def main():
    window(200, 200, background='#000')
    o = oval(20, 20, 180, 180, fill=from_rgb(100, 0, 0))
    fi = 0
    while True:
        sleep(.02)
        d = 80 * math.cos(fi)
        e = 80 * math.cos(fi * math.pi)
        coords(o, 100 - e, 100 - d, 100 + e, 100 + d)
        configure(o, fill=from_hsl(h=fi * 360, s=100, l=100))
        fi += .01


if __name__ == '__main__':
    main()
