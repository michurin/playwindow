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


class Window(object):

    # It is not smart, but all UI code must be in the same thread.
    # So, polling.

    # Methods in UI thread

    def __init__(self, startup_lock):
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
        root.after('idle', self.__mainloop_starged)
        root.mainloop()

    def __mainloop_starged(self):
        self.__canvas.focus_set()
        self.__root.wm_title('playwindow')
        globals()['WIN'] = self
        self.__startup_lock.release()
        del self.__startup_lock
        self.__update()

    def __update(self):
        if self.__update_period < 29:
            # after     0  3  7 12 18 26 36 49 66 88
            # interval  3  4  5  6  8 10 13 17 22 29 29 29...
            self.__update_period += self.__update_period // 3
        try:
            while True:
                task = self.__queue.get_nowait()
                #print('TASK: ' + repr(task))
                t, m, a, kv = task
                if t == 'canvas':
                    getattr(self.__canvas, m)(*a, **kv)
                elif t == 'root':
                    getattr(self.__root, m)(*a, **kv)
                else:
                    raise Exception('t=' + t)
                self.__root.update_idletasks()
                self.__update_period = 3
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
        self.__task('root', 'geometry', (('%dx%d' % (w, h)),), {})

    def background(self, color):
        self.__task('canvas', 'configure', (), {'bg': color})

    def line(self, *a, **kv):
        self.__task('canvas', 'create_line', a, kv)

    def rect(self, *a, **kv):
        self.__task('canvas', 'create_rectangle', a, kv)

    def oval(self, *a, **kv):
        self.__task('canvas', 'create_oval', a, kv)

    def text(self, *a, **kv):
        self.__task('canvas', 'create_text', a, kv)

    def image(self, *a, **kv):
        self.__task('canvas', 'create_image', a, kv)

    def move(self, *a):
        self.__task('canvas', 'move', a, {})

    def coords(self, *a):
        self.__task('canvas', 'coords', a, {})

    def config(self, *a, **kv):
        self.__task('canvas', 'itemconfigure', a, kv)

    def top(self, *a):
        self.__task('canvas', 'tag_raise', a, {})

    def bottom(self, *a):
        self.__task('canvas', 'tag_lower', a, {})

    def delete(self, *a):
        self.__task('canvas', 'delete', a, {})

    # events

    @property
    def size(self):
        return (self.__width, self.__height)

    @property
    def keys(self):
        return self.__events.keys

    @property
    def event(self):
        return self.__events.event

    @property
    def event_nowait(self):
        return self.__events.event_nowait

    def event_clear(self):
        self.__events.event_clear()

    @property
    def pointer_position(self):
        return self.__events.pointer_position

    @property
    def buttons(self):
        return self.__events.buttons

    # tools

    def create_image(self, *a, **kv):
        return Image(*a, **kv)


def setup():
    lock = threading.Lock()
    lock.acquire()
    threading.Thread(target=Window, args=(lock,), daemon=True).start()
    with lock: pass # main thread must wait for slave


setup()
