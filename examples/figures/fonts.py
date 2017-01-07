#!/usr/bin/python3
# coding: U8


from playwindow import window, text

window(width=600, height=600, background='#000')

y = 20
for size in (5, 6, 7, 8, 10, 12, 14, 16):
    text(20, y, text='font size = %d' % size, anchor='w', font={'size': size}, fill='#fff')
    y += 24

y += 24

for weight in ('normal', 'bold'):
    text(20, y, text='font weight = %s' % weight, anchor='w', font={'weight': weight}, fill='#fff')
    y += 24

y += 24

for slant in ('roman', 'italic'):
    text(20, y, text='font slant = %s' % slant, anchor='w', font={'slant': slant}, fill='#fff')
    y += 24

y += 24

for underline in (0, 1):
    text(20, y, text='font underline = %r' % underline, anchor='w', font={'underline': underline}, fill='#fff')
    y += 24

y += 24

for overstrike in (0, 1):
    text(20, y, text='font overstrike = %r' % overstrike, anchor='w', font={'overstrike': overstrike}, fill='#fff')
    y += 24

y += 24

text(20, y, text='bold, italic, underline, size=14', anchor='w', font={
    'weight': 'bold',
    'slant': 'italic',
    'underline': 1,
    'size': 14
}, fill='#fff')
