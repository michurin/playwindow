# coding: utf-8


import tkinter
import hashlib


class Image:

    # When a PhotoImage object is garbage-collected by Python,
    # the image is cleared even if it’s being displayed(!).
    # To avoid this, the program must keep an extra reference
    # to the image object. Here.
    __ref_keeper = {}

    def __init__(self, colormap, palette, scale=None):
        self.__tk_image = None
        self.__colormap = colormap
        self.__palette = palette
        self.__scale = scale
        self.__hash = hashlib.md5((
            '\n'.join(colormap) + '\n' +
            '\n'.join(x + ':' + palette[x] for x in sorted(palette.keys()))
        ).encode()).hexdigest()

    def __str__(self):
        '''
        __str__ is important part of native
        tkinter.PhotoImage API
        '''
        try:
            return self.__ref_keeper[self.__hash].name
        except KeyError:
            pass
        pi = tkinter.PhotoImage()
        for y in range(len(self.__colormap) - 1, -1, -1):
            for x, c in enumerate(self.__colormap[y]):
                if c != '.':
                    pi.put(self.__palette.get(c, '#f00'), to=(x, y))
        if not self.__scale is None:
            pi = pi.zoom(self.__scale, self.__scale)
        self.__ref_keeper[self.__hash] = pi
        return pi.name


def test():
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg='#888')
    canvas.pack(fill='both', expand=True)
    i = Image([
        'A...',
        '.A.A',
        '..A.'
    ], {
        'A': '#0f0'
    })
    canvas.create_image(70, 30, image=i)
    root.mainloop()


if __name__ == '__main__':
    test()
