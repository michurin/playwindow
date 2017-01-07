#!/usr/bin/python3
# coding: U8


from playwindow import window, photo_create, photo_copy, image, oval, text, wait_for_move, configure, overlapping

window(width=400, height=400, background='#000')

n=None
r='#f00'
b='#000'
sprite = photo_create([
    [r,n,r,n,n,n,n,n,r,n,r],
    [r,n,r,n,n,n,n,n,r,n,r],
    [n,r,n,n,n,n,n,n,n,r,n],
    [n,r,n,r,r,r,r,r,n,r,n],
    [n,n,r,r,b,r,b,r,r,n,n],
    [n,n,n,r,r,r,r,r,n,n,n],
    [n,n,n,n,r,n,r,n,n,n,n],
    [n,n,n,r,r,n,r,r,n,n,n],
], zoom=5)

dict_of_anchors = dict()

for x, y, anchor in (
        (100, 100, 'nw'), (200, 100,      'n'), (300, 100, 'ne'),
        (100, 200,  'w'), (200, 200, 'center'), (300, 200, 'e'),
        (100, 300, 'sw'), (200, 300,      's'), (300, 300, 'se'),
    ):
    oid = image(x, y, sprite, anchor=anchor)
    oval(x - 6, y - 6, x + 6, y + 6, fill='#0f0', width=0)
    dict_of_anchors[oid] = 'anchor=%r' % anchor

default_label = 'move mouse to get value of anchor'

txt = text(200, 50, text=default_label, fill='#ccc', font={'size': 12, 'weight': 'bold'})

while True:
    e = wait_for_move()
    oids = overlapping(e.x-1, e.y-1, e.x+1, e.y+1)
    if len(oids) > 0:
        oid = oids[0]
    else:
        oid = 'fake'
    configure(txt, text=dict_of_anchors.get(oid, default_label))
