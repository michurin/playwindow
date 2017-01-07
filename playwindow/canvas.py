# coding: U8


from playwindow.ipc import tk_call
from playwindow.util import public


@public
def cls():
    return bool(tk_call(
        'canvas_manipulator',
        'delete',
        'all'
    ))


@public
def line(*xy, fill='#888', width=5, capstyle='round', joinstyle='round', smooth=False):
    return int(tk_call(
        'canvas_manipulator',
        'create',
        'line',
        *xy,
        fill=fill,
        width=width,
        capstyle=capstyle,
        joinstyle=joinstyle,
        smooth=bool(smooth)
    ))


@public
def oval(x1, y1, x2, y2, *, fill=None, width=3, outline='#777'):
    return int(tk_call(
        'canvas_manipulator',
        'create',
        'oval',
        x1, y1, x2, y2,
        fill=fill,
        width=width,
        outline=outline
    ))


@public
def polygon(*xy, fill='#888', width=3, smooth=False, joinstyle='round', outline='#fff'):
    return int(tk_call(
        'canvas_manipulator',
        'create',
        'polygon',
        *xy,
        fill=fill,
        width=width,
        smooth=bool(smooth),
        joinstyle=joinstyle,
        outline=outline
    ))


@public
def rectangle(*xy, fill=None, width=3, outline='#777'):
    return int(tk_call(
        'canvas_manipulator',
        'create',
        'rectangle',
        *xy,
        fill=fill,
        width=width,
        outline=outline
    ))


@public
def text(x, y,
        text='[no text]',
        *,
        fill='#888',
        anchor=None,
        font=None,
        justify=None,
        width=None
    ):
    return int(tk_call(
        'canvas_manipulator',
        'create',
        'text',
        x, y,
        text=text,
        fill=fill,
        anchor=anchor,
        font=font,
        justify=justify,
        width=width
    ))


@public
def image(x, y, image, *, anchor):
    return int(tk_call(
        'canvas_manipulator',
        'create',
        'image',
        x, y,
        image=image,
        anchor=anchor
    ))


@public
def delete(*oid):
    return bool(tk_call(
        'canvas_manipulator',
        'delete',
        *oid
    ))


@public
def find_all():
    return tuple(map(
        int,
        tk_call('canvas_manipulator', 'find', 'all').split()
    ))


@public
def postscript(file_name):
    return bool(tk_call('canvas_manipulator', 'postscript', file=file_name))


@public
def raise_item(oid):
    return bool(tk_call('canvas_manipulator', 'raise', oid))


@public
def lower_item(oid):
    return bool(tk_call('canvas_manipulator', 'lower', oid))


@public
def item_type(oid):
    return str(tk_call('canvas_manipulator', 'type', oid))


@public
def configure(
        oid,
        *,
        capstyle=None,
        fill=None,
        joinstyle=None,
        outline=None,
        smooth=None,
        text=None,
        width=None,
        justify=None
    ):
    return bool(tk_call(
        'canvas_manipulator',
        'itemconfigure',
        oid,
        capstyle=capstyle,
        fill=fill,
        joinstyle=joinstyle,
        outline=outline,
        smooth=smooth,
        text=text,
        width=width,
        justify=justify
    ))


@public
def coords(oid, *xy):
    return bool(tk_call('canvas_manipulator', 'coords', oid, *xy))


@public
def move(oid, x, y):
    return bool(tk_call('canvas_manipulator', 'move', oid, x, y))


@public
def moveto(oid, x, y):
    return bool(tk_call('canvas_manipulator', 'moveto', oid, x, y))


@public
def overlapping(x1, y1, x2, y2):
    return tuple(int(oid) for oid in tk_call(
        'canvas_manipulator',
        'find',
        'overlapping',
        x1, y1, x2, y2
    ).split())
