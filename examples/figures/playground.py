#!/usr/bin/python3
# coding: U8


import math
import random
from playwindow import window, line, oval, rectangle, polygon, move


window(width=300, height=300, background='#06f')

# ground
line(10, 290, 290, 290, fill='#0f0', width=20)

# house
rectangle(70, 130, 220, 280)
polygon(70, 130, 220, 130, 145, 60, 70, 130, fill='#f00')
rectangle(100, 200, 140, 280, fill='#080')
rectangle(160, 200, 200, 240, fill='#008')

# sun
for i in range(16):
    fi = math.pi * 2 * i / 16
    line(50, 50, 50 + 140 * math.sin(fi), 50 + 140 * math.cos(fi), fill='#ff0')
oval(20, 20, 80, 80, fill='#ff0')

# clouds
for s in 0, 160:
    for i in range(18):
        x = random.random() * 50 - s
        y = random.random() * 30
        o = oval(220, 20, 240, 40, fill='#fff')
        move(o, x, y)
