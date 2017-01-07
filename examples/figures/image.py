#!/usr/bin/python3
# coding: U8


from playwindow import window, photo_create, photo_copy, image, oval

window(width=600, height=200, background='#000')

oval(0, 0, 100, 100, fill='#080', outline='#0f0')

p = photo_create([['#f00', None], ['#fff', '#f00']])
print('p=%r' % p)
p2 = photo_copy(p, zoom=10)
image(20, 20, p2)
image(24, 24, p2)

n=None
r='#f00'
b='#000'
p3 = photo_create([
    [r,n,r,n,n,n,n,n,r,n,r],
    [r,n,r,n,n,n,n,n,r,n,r],
    [n,r,n,n,n,n,n,n,n,r,n],
    [n,r,n,r,r,r,r,r,n,r,n],
    [n,n,r,r,b,r,b,r,r,n,n],
    [n,n,n,r,r,r,r,r,n,n,n],
    [n,n,n,n,r,n,r,n,n,n,n],
    [n,n,n,r,r,n,r,r,n,n,n],
], zoom=4)
image(100, 24, p3)
