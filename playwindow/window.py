# coding: utf-8


from playwindow.events import Events
from playwindow.image import Image


import os
import signal
import tkinter
import threading
import queue


__all__ = 'WIN'


WIN = None


class default_params:

    __common_params = {
        'dash',
        'dashoffset',
        'fill',
        'outline',
        'offset',
        'outlinestipple',
        'stipple',
        'tags',
        'width'}

    def __init__(me, *allowed_params):
        me.__allowed_params = me.__common_params | set(allowed_params)

    def __call__(me, f):
        def g(self, *a, **orig_kv):
            kv = {}
            for k in me.__allowed_params:
                try:
                    kv[k] = orig_kv[k]
                    del orig_kv[k]
                except KeyError:
                    try:
                        kv[k] = self.defaults[k]
                    except KeyError:
                        pass
            if orig_kv:
                print('WARN', orig_kv)
            return f(self, *a, **kv)
        g.__doc__ = '%s\nAllowed attributes:\n%s' % (
            f.__doc__,
            ', '.join(sorted(me.__allowed_params))
        )
        g.__name__ = f.__name__
        return g


class Window(object):

    # It is not smart, but all UI code must be in the same thread.
    # So, polling.

    # Methods in UI thread

    def __init__(self, startup_lock):
        self.defaults = {} # public
        self.__startup_lock = startup_lock
        self.__queue = queue.Queue()
        self.__update_period = 5
        self.__width = -1
        self.__height = -1
        events = Events()
        self.__events = events
        root = tkinter.Tk()
        self.__root = root
        canvas = tkinter.Canvas(root, bg='black', bd=0, highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        canvas.bind('<Destroy>', self.__on_destroy)
        canvas.bind('<KeyPress>', events.on_key_press)
        canvas.bind('<KeyRelease>', events.on_key_release)
        canvas.bind('<Configure>', self.__on_configure)
        canvas.bind('<FocusIn>', events.on_enter)
        canvas.bind('<FocusOut>', events.on_leave)
        canvas.bind('<Motion>', events.on_motion)
        canvas.bind('<ButtonPress>', events.on_button_press)
        canvas.bind('<ButtonRelease>', events.on_button_release)
        root.bind('<FocusIn>', lambda e: canvas.focus_set())
        #print(repr(list(filter(lambda x: 'gra' in x, dir(canvas)))))
        self.__canvas = canvas
        root.after('idle', self.__mainloop_started)
        root.mainloop()

    def __mainloop_started(self):
        self.__canvas.focus_set()
        self.__root.wm_title('playwindow')
        globals()['WIN'] = self
        self.__startup_lock.release()
        del self.__startup_lock
        self.__update()

    def __update(self):
        if self.__update_period < 97: ## CONST 97
            # poll interval formula
            # x[0] = 10
            # x[n+1] = x[n] + x[n]//4
            # after      0 10 22 37 55 77 104 137 178 229 292 370
            # interval  10 12 15 18 22 27  33  41  51  63  78  97 97 97
            self.__update_period += self.__update_period // 4 ## CONST 4
        try:
            while True:
                task = self.__queue.get_nowait() # get or break loop
                #print('TASK: ' + repr(task))
                t, m, a, kv = task
                if t == 'canvas':
                    getattr(self.__canvas, m)(*a, **kv)
                elif t == 'root':
                    getattr(self.__root, m)(*a, **kv)
                else:
                    raise Exception('t=' + t)
                self.__root.update_idletasks()
                self.__update_period = 10 ## CONST 10
        except queue.Empty:
            pass
        self.__root.after(self.__update_period, self.__update)

    def __on_destroy(self, event):
        os.kill(os.getpid(), signal.SIGKILL)

    def __on_configure(self, event):
        self.__width = event.width
        self.__height = event.height

    # Methods in main (or any other) thread

    def __task(self, *task):
        self.__queue.put(task)

    def resize(self, w, h):
        '''Resize main window'''
        self.__task('root', 'geometry', (('%dx%d' % (w, h)),), {})

    def background(self, color):
        '''Set background of main window'''
        self.__task('canvas', 'configure', (), {'bg': color})

    @default_params(
        'extent',
        'start',
        'style')
    def arc(self, *a, **kv):
        '''Draw arc. A section of an oval delimited by two angles'''
        self.__task('canvas', 'create_arc', a, kv)

    @default_params(
        'arrow',
        'arrowshape',
        'capstyle',
        'joinstyle',
        'smooth',
        'splinesteps')
    def line(self, *a, **kv):
        '''Draw line.'''
        self.__task('canvas', 'create_line', a, kv)

    @default_params(
        'joinstyle',
        'smooth',
        'splinesteps')
    def polygon(self, *a, **kv):
        '''Draw polygon.'''
        self.__task('canvas', 'create_polygon', a, kv)

    @default_params()
    def rect(self, *a, **kv):
        '''Draw rectangle.'''
        self.__task('canvas', 'create_rectangle', a, kv)

    @default_params()
    def oval(self, *a, **kv):
        '''Draw oval.'''
        self.__task('canvas', 'create_oval', a, kv)

    @default_params(
        'anchor',
        'font',
        'justify',
        'text')
    def text(self, *a, **kv):
        '''Draw text.'''
        self.__task('canvas', 'create_text', a, kv)

    @default_params(
        'anchor',
        'image')
    def image(self, *a, **kv):
        '''Draw image prepared by `create_image` method.'''
        self.__task('canvas', 'create_image', a, kv)

    def move(self, *a):
        '''Move each of the items given by tag by adding dx and dy to x and y.'''
        self.__task('canvas', 'move', a, {})

    def coords(self, *a):
        '''Modify the coordinates that define an item'''
        self.__task('canvas', 'coords', a, {})

    def config(self, *a, **kv):
        '''Modify the configuration options of the item'''
        self.__task('canvas', 'itemconfigure', a, kv)

    def top(self, *a):
        '''Raise an item'''
        self.__task('canvas', 'tag_raise', a, {})

    def bottom(self, *a):
        '''Lower an item'''
        self.__task('canvas', 'tag_lower', a, {})

    def delete(self, *a):
        '''Delete an item'''
        self.__task('canvas', 'delete', a, {})

    # events

    @property
    def size(self):
        '''Window geometry tuple (width, height)'''
        return (self.__width, self.__height)

    @property
    def keys(self):
        '''Map of currently pressed keys'''
        return self.__events.keys

    @property
    def event(self):
        '''Get/wait next event'''
        return self.__events.event

    @property
    def event_nowait(self):
        '''Return event or None'''
        return self.__events.event_nowait

    def event_clear(self):
        '''Clear events queue'''
        self.__events.event_clear()

    @property
    def pointer_position(self):
        '''Get current pointer position'''
        return self.__events.pointer_position

    @property
    def buttons(self):
        '''Get current mouse buttons state'''
        return self.__events.buttons

    # tools

    def create_image(self, *a, **kv):
        '''Create image'''
        return Image(*a, **kv)


def setup():
    lock = threading.Lock()
    lock.acquire()
    threading.Thread(target=Window, args=(lock,), daemon=True).start()
    with lock: pass # main thread must wait here for slave


setup()
