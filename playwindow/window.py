# coding: U8


from playwindow.ipc import tk_call
from playwindow.util import public


@public
def window_size(width, height):
    return window(width, height)


@public
def window_color(color):
    return window(background=color)


@public
def window_cursor(cursor):
    return window(cursor=cursor)


@public
def window(width=None, height=None, *, background=None, cursor=None, title=None):
    '''
    list of cursors can be found here:
    https://www.tcl.tk/man/tcl8.6/TkCmd/cursors.htm
    use cursor='none' to hide pointer
    '''
    tk_call(
        'canvas_manipulator',
        'configure',
        width=width,
        height=height,
        background=background,
        cursor=cursor
    )
    if title is not None:
        window_title(title)
    return True


@public
def window_title(title):
    return bool(tk_call('wm', 'title', '.', title))


@public
def window_close():
    return bool(tk_call('stop'))
