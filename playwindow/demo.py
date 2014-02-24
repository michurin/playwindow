# coding: utf-8


from playwindow import win
from time import sleep
from random import randrange, random
from math import sin, pi as PI


def demo_setup():
    print('- demo_setup()')
    win.delete('all')
    win.resize(400, 300)
    win.background('#222222')
    win.text(10, 10, fill='#ffffff', text=(
        'At very beginning\n'
        'we clear and setup window\n'
        'size and background.\n\n'
        'Press any key or click to continue.'
    ), anchor='nw')
    win.event_clear()
    e = win.event
    win.delete('all')


def demo_draw_basics():
    print('- demo_draw_basics()')
    w, h = win.size
    win.line(20, 20, w - 20, h - 20, width=3, fill='#440044', tags=('my_line',))
    win.oval(50, 50, 150, 250, width=0, fill='#444444', tags=('my_ovals',))
    win.oval(250, 50, 350, 250, width=4, fill='#000000', outline='#005555', tags=('my_ovals',))
    win.text(10, 10, fill='#ffffff', text='Drawing.', anchor='nw', tags=('label',))
    win.event_clear()
    e = win.event

    win.config('label', fill='#999999', text='We can modify elements (text)')
    win.event_clear()
    e = win.event

    win.config('my_line', width=40)
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
    for t in range(20, w-20, 8):
        sleep(.05)
        win.coords('my_line', t, 20, w - t, h - 20)
    win.config('label', text='Alternate coordinates... done.')
    win.event_clear()
    e = win.event

    win.delete('all')


def demo_draw_shapes():
    print('- demo_draw_shapes()')
    win.text(10, 10, fill='#ffffff', text='Drawing shapes.', anchor='nw', tags=('label',))
    win.event_clear()
    e = win.event
    win.delete('all')

    w, h = win.size
    y1 = 60
    y2 = h - 30
    x = 30
    step = (w - x * 2) / 17
    win.line(x, y1, x, y2, fill='#880088', width=3)
    x += step
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, arrow='first')
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, arrow='last')
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, arrow='both')
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, arrow='first',
        arrowshape=(20, 30, 10))
    x += step
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=15, capstyle='butt')
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=15, capstyle='projecting')
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=15, capstyle='round')
    x += step
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, dash=(5,))
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, dash=(5, 10))
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, dash=(5, 5, 2, 5))
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, dash=(5, 2, 2, 2, 2, 2))
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=3, dash=(5, 2, 2, 2, 2, 2), dashoffset=2)
    x += step
    x += step
    win.line(x, y1, x, y2, fill='#880088', width=10,
        dash=(6,), arrow='first', arrowshape=(20, 20, 10), capstyle='round')

    win.text(10, 10, fill='#999999', anchor='nw',
        text='Lines.\nArrows. Custom arrows.\nCapstyle.\nDash.')
    win.event_clear()
    e = win.event
    win.delete('all')

    w, h = win.size
    y1 = 60
    y2 = h - 30
    x1 = 30
    x2 = x1 + (y2 - y1) / 2
    step = (w - x2 - x1) / 2
    win.arc(x1, y1, x2, y2, fill='#880088', start=180, extent=45)
    x1 += step
    x2 += step
    win.arc(x1, y1, x2, y2, fill='#880088', start=0, extent=135,
       outline='#ff00ff', width=5)
    x1 += step
    x2 += step
    win.arc(x1, y1, x2, y2, fill='#880088', start=-135, extent=180,
       outline='#ffffff', width=2, dash=(5, 10))

    win.text(10, 10, fill='#999999', anchor='nw', text='Arcs.')
    win.event_clear()
    e = win.event
    win.delete('all')

    w, h = win.size
    xo, yo = w // 2, h // 2
    r = min(xo, yo)/2 - 20
    step = (r - 10)/4
    win.polygon(
        xo + r, yo - r - r,
        xo + r + r, yo,
        xo + r, yo + r + r,
        xo - r - r, yo + r + r,
        xo - r - r, yo - r - r,
        outline='#888888', smooth='bezier', width=3, fill='#558855'
    )
    r -= step
    r -= step
    win.polygon(
        xo + r, yo - r - r,
        xo + r + r, yo,
        xo + r, yo + r + r,
        xo - r - r, yo + r + r,
        xo - r - r, yo - r - r,
        outline='#888888', joinstyle='round', width=10, fill='#555555'
    )
    r -= step
    win.polygon(
        xo + r, yo - r - r,
        xo + r + r, yo,
        xo + r, yo + r + r,
        xo - r - r, yo + r + r,
        xo - r - r, yo - r - r,
        outline='#888888', width=10, fill='#333333'
    )
    r -= step
    win.polygon(
        xo + r, yo - r - r,
        xo + r + r, yo,
        xo + r, yo + r + r,
        xo - r - r, yo + r + r,
        xo - r - r, yo - r - r,
        outline='#888888', width=1, fill='#111111'
    )

    win.text(10, 10, fill='#999999', anchor='nw', text='Polygons and bezier.')
    win.event_clear()
    e = win.event
    win.delete('all')


def demo_bitmaps():
    print('- demo_bitmaps()')
    win.text(10, 10, fill='#ffffff', text='Images.', anchor='nw', tags=('label',))
    win.event_clear()
    e = win.event

    win.config('label', fill='#999999', text='Simple drawing.')
    w, h = win.size
    win.text(10, h - 10, fill='#999900', text='''First image definition is:
win.create_image(
    [
        'A.', # bit map
        '.B'
    ], {
        'A': '#f00', # color map
        'B': '#0f0',
    },
    10 # scale factor
)
''', anchor='sw', tags=('info',), font='Mono 9')

    simple_image = win.create_image(
        [
            'A.',
            '.B'
        ], {
            'A': '#f00',
            'B': '#0f0',
        },
        10
    )
    win.image(20, 60, image=simple_image)
    ant = win.create_image(
        [
            '.....ABABA',
            '....AAAAAAA',
            'A....AAAAA....A',
            '.AA....A....AA',
            '...AA.AAA.AA',
            'AA....AAA....AA',
            '..AAAA.A.AAAA',
            '.......A',
            '..AAAA.A.AAAA',
            'AA.....A.....AA',
            '.....AAAAA',
            '....AAAAAAA',
            '....AAAAAAA',
            '.....AAAAA',
            '......AAA'
        ], {
            'A': '#960',
            'B': '#ff0'
        },
        2
    )
    win.image(80, 60, image=ant, tags='ant')
    ant_r = win.create_image(
        [
            '.....ABABA',
            'A...AAAAAAA',
            '.A...AAAAA',
            '..A....A....AAA',
            '...AA.AAA.AA',
            '......AAA....AA',
            'AAAAAA.A.AAAA',
            '.......A',
            'AAAAAA.A.AAAA',
            '.......A.....AA',
            '.....AAAAA',
            '....AAAAAAA',
            '....AAAAAAA',
            '.....AAAAA',
            '......AAA'
        ], {
            'A': '#960',
            'B': '#ff0'
        },
        2
    )
    win.image(120, 60, image=ant_r, tags='ant')
    ant_l = win.create_image(
        [
            '.....ABABA',
            '....AAAAAAA...A',
            '.....AAAAA...A',
            'AAA....A....A',
            '...AA.AAA.AA',
            'AA....AAA',
            '..AAAA.A.AAAAAA',
            '.......A',
            '..AAAA.A.AAAAAA',
            'AA.....A',
            '.....AAAAA',
            '....AAAAAAA',
            '....AAAAAAA',
            '.....AAAAA',
            '......AAA'
        ], {
            'A': '#960',
            'B': '#f00'
        },
        2
    )
    win.image(160, 60, image=ant_l, tags='ant')
    win.event_clear()
    e = win.event

    win.delete('info')
    win.config('label', text='You can change bitmap any time...')
    for i in range(30):
        sleep(.05)
        win.config('ant', image=[ant_l, ant, ant_r, ant][i % 4])
    win.config('label', text='You can change bitmap any time...\nand move...')
    win.move('ant', 0, 60)
    for i in range(60):
        sleep(.05)
        win.config('ant', image=[ant_l, ant, ant_r, ant][i % 4])
        win.move('ant', 0, -1)
    win.config('label', text='You can change bitmap any time...\nand move... done.')
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


def intro(message):
    print('- intro()')
    win.delete('all')
    win.resize(400, 300)
    win.background('#020')
    class Taraxacum:
        def __init__(self, x, y, base):
            self.c = random() * 2 * PI
            self.dc = .1 - random() * .05
            self.r = 10 + random() * 4
            self.xo = x
            self.yo = y
            self.base = base
            win.line(
                0, 0, 0, 0,
                fill='#480',
                width=4 + random() * 2,
                capstyle='round',
                tags=base + '_L')
            win.oval(
                0, 0, 0, 0,
                width=2,
                fill='#777',
                outline='#fff',
                tags=base + '_O')
            self()
        def __call__(self):
            self.c += self.dc
            dx = 10 * sin(self.c)
            win.coords(
               self.base + '_L',
               self.xo, self.yo, self.xo - dx, self.yo - 30)
            win.coords(
               self.base + '_O',
               self.xo - dx - self.r,
               self.yo - 30 - self.r,
               self.xo - dx + self.r,
               self.yo - 30 + self.r)
    tt = []
    for y in range(80, 300, 10):
        tt.append(Taraxacum(randrange(20, 380), y, 'tag_%d' % y))
    win.text(
        20, 20,
        fill='#ff0',
        text=message,
        anchor='nw',
        font='Arial 20 bold')
    win.text(
        390, 290,
        fill='#ff0',
        text='Click to continue',
        anchor='se')
    while win.buttons: pass
    while not win.buttons:
        sleep(.05)
        for t in tt:
            t()
    while win.buttons: pass
    win.delete('all')


def demo_all():
    print('Follow instructions in application window.')
    print('View source code here: %s' % __file__)
    intro('Welcome!')
    demo_setup()
    demo_draw_basics()
    demo_draw_shapes()
    demo_bitmaps()
    demo_events()
    intro('See you here!')


if __name__ == '__main__':
    demo_all()
