# coding: U8


from playwindow.ipc import tk_call
from playwindow.util import public


class ImageFactory(object):

    def __init__(self):
        self.serial_number = 0

    def __call__(self):
        name = 'IM_%s' % self.serial_number
        self.serial_number += 1
        tk_call('image', 'create', 'photo', name)
        return name


image_factory = ImageFactory()


@public
def photo_create(data, *, zoom=None):
    name = image_factory()
    y = 0
    for l in data:
        x = 0
        for c in l:
            if c is not None:
                tk_call(name, 'put', c, '-to', x, y)
            x += 1
        y += 1
    if zoom is not None:
        zoomed = photo_copy(name, zoom=zoom)
        photo_delete(name)
        name = zoomed
    return name


@public
def photo_delete(*names):
    return bool(tk_call('image', 'delete', *names))


@public
def photo_copy(source, *, zoom=None):
    target = image_factory()
    tk_call(target, 'copy', source, zoom=zoom)
    return target
