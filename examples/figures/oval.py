#!/usr/bin/python3
# coding: U8


from playwindow import window, oval


window(width=300, height=300, background='#000')

oval(20, 20, 160, 160, fill='#777')
oval(140, 20, 280, 160, width=10, outline='#f00')
oval(20, 140, 280, 280, width=1, outline='#0f0', fill='#070')
