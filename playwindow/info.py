# coding: U8


from playwindow.ipc import tk_call
from playwindow.util import public


@public
def pointer_xy():
    return tuple((
        int(tk_call('winfo', 'pointer' + d, '.')) -
        int(tk_call('winfo', 'root' + d, '.r'))
    ) for d in 'xy')


@public
def debug(debug_mode=True):
    tk_call.debug(debug_mode)
