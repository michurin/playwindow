#!/usr/bin/python3
# coding: U8


from playwindow import window, text, wait, configure, coords, EventConfigure

window(width=400, height=400, background='#000')

font_info = {'size': 12, 'weight': 'bold'}
title = text(200, 50, text='Resize the window!', fill='#999', font=font_info, justify='center')
label = text(200, 100, text='[event...]', fill='#ccc', font=font_info, justify='center')

while True:
    e = wait()
    if type(e) is EventConfigure:
        xo = e.width // 2
        yo = e.height // 2
        coords(title, xo, yo - 25)
        coords(label, xo, yo + 25)
        configure(title, width=e.width)
        configure(label, text=repr(e), width=e.width)
