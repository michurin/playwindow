# coding: utf-8


from playwindow import win
from time import sleep


def demo_setup():
    print('- demo_setup()')
    win.delete('all')
    win.resize(300, 200)
    win.background('#222222')
    win.text(10, 10, fill='#ffffff', text=(
        'Wellcome!\n\n'
        'We clear and setup window\n'
        'size and background.\n\n'
        'Press any key or click to continue.'
    ), anchor='nw')
    win.event_clear()
    e = win.event
    win.delete('all')


def demo_draw():
    print('- demo_draw()')
    w, h = win.size
    win.line(20, 20, w - 20, h - 20, width=3, fill='#440044', tags=('my_line',))
    win.oval(50, 50, 150, 150, width=0, fill='#444444', tags=('my_ovals',))
    win.oval(150, 50, 250, 150, width=4, fill='#000000', outline='#005555', tags=('my_ovals',))
    win.text(10, 10, fill='#ffffff', text='Drawing.', anchor='nw', tags=('label',))
    win.event_clear()
    e = win.event

    win.config('label', fill='#999999', text='We can modify elements (text)')
    win.event_clear()
    e = win.event

    win.config('my_line', width=20)
    win.config('label', text='We can modify elements (width)')
    win.event_clear()
    e = win.event

    win.config('my_line', fill='#660000')
    win.config('label', text='We can modify elements (color)')
    win.event_clear()
    e = win.event

    win.config('my_line', capstyle='round')
    win.config('label', text='We can modify elements (capstyle)')
    win.event_clear()
    e = win.event

    win.top('my_line')
    win.top('label')
    win.config('label', text='We can raise elements...')
    win.event_clear()
    e = win.event

    win.bottom('my_line')
    win.config('label', text='...and lower')
    win.event_clear()
    e = win.event

    win.config('label', text='Move...')
    for _ in range(30):
        sleep(.05)
        win.move('my_ovals', 0, 1)
        win.move('my_line', 1, 0)
    win.config('label', text='Move... and back...')
    for _ in range(30):
        sleep(.05)
        win.move('my_ovals', 0, -1)
        win.move('my_line', -1, 0)
    win.config('label', text='Move... and back... done.')
    win.event_clear()
    e = win.event

    win.delete('my_ovals')
    win.config('label', text='Delete (by tags)')
    win.event_clear()
    e = win.event

    win.config('label', text='Alternate coordinates...')
    for t in range(20, w-20, 4):
        sleep(.05)
        win.coords('my_line', t, 20, w - t, h - 20)
    win.config('label', text='Alternate coordinates... done.')
    win.event_clear()
    e = win.event

    win.delete('all')


def demo_events():
    print('- demo_events()')
    win.text(10, 10, fill='#ffffff', text='Events.', anchor='nw', tags=('label',))
    win.event_clear()
    e = win.event

    w, h = win.size

    win.config('label', fill='#999999', text='Click...\nPress [space] to continue.')
    win.text(10, h - 10, fill='#999900', text='', anchor='sw', tags=('info',))
    win.event_clear()
    while True:
        e = win.event
        win.config('info', text=repr(e))
        if e.tp == 'button_press':
            win.oval(
                e.x - 10, e.y - 10, e.x + 10, e.y + 10,
                width=2, fill='#000044', outline='#777777')
        if e.tp == 'key_press':
            if e.sym == 'space':
                break
    win.delete('all')

    while 65 in win.keys:
        pass
    win.text(10, 10, fill='#999999', text=(
        'States.\n'
        'Move mouse,\n'
        'press keys on keyboard and\n'
        'mouse buttons.\n'
        'Press [space] to continue.'
    ), anchor='nw', tags=('label',))
    win.text(10, h - 10, fill='#999900', text='', anchor='sw', tags=('info',))
    win.rect(0, 5, 34, 20,
        width=2, fill='#000044', outline='#777777', tags=('main', 'ovals'))
    win.rect(0, -10, 10, 0,
        width=0, fill='#440044', tags=('oval-1', 'ovals'))
    win.rect(12, -10, 22, 0,
        width=0, fill='#440044', tags=('oval-2', 'ovals'))
    win.rect(24, -10, 34, 0,
        width=0, fill='#440044', tags=('oval-3', 'ovals'))
    prev_x = 34/2
    prev_y = 10
    while True:
        sleep(.04)
        b = win.buttons
        p = win.pointer_position
        k = win.keys
        if 65 in k:
            break
        win.config('info', text=(
            'win.buttons=%s\nwin.pointer_position=%s\nwin.keys=%s' % tuple(map(repr, (b, p, k)))
        ))
        if p:
            x, y = p
            dx = x - prev_x
            dy = y - prev_y
            win.move('ovals', dx, dy)
            for n in range(1, 4):
                if n in b:
                    clr = '#ff0000'
                else:
                    clr = '#440044'
                win.config('oval-%d' % n, fill=clr)
            prev_x = x
            prev_y = y
    win.delete('all')


def demo_fonts():
    print('- demo_fonts()')
    win.text(
        10, 10,
        fill='#ffffff',
        text='Bye!',
        anchor='nw',
        font='Arial 20 bold',
        tags=('label',))
    win.event_clear()


def demo_all():
    print('Follow instructions in application window.')
    print('View source code here: %s' % __file__)
    demo_setup()
    demo_draw()
    demo_events()
    demo_fonts()


if __name__ == '__main__':
    demo_all()
    e = win.event
