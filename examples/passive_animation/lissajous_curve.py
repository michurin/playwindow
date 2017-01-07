#!/usr/bin/python3
# coding: U8


import math

from playwindow import window, sleep, polygon, coords


POINTS_COUNT = 100


window(width=400, height=400, background='#000')


oid = polygon(*([0] * (POINTS_COUNT * 2)), outline='#0f0', fill=None, smooth=1, width=8)

q = 0
while True:
    q += 0.03
    coor = []
    for i in range(POINTS_COUNT):
        fi = math.pi * 2 * i / POINTS_COUNT
        x = math.sin(fi * 5)
        y = math.cos(fi * 4 + q)
        coor.append(200 + 160 * x)
        coor.append(200 + 160 * y)
    coords(oid, *coor)
    sleep(0.05)
