#!/usr/bin/python3
# coding: utf-8


import threading


__all__ = 'Events',


class KeyPress(object):

    def __init__(self, event):
        self.tp = 'key_press'
        self.code = event.keycode
        self.sym = event.keysym

    def __str__(self):
        return self.sym

    def __repr__(self):
        return '<%s code=%s sym="%s">' % (self.tp, self.code, self.sym)


class ButtonPress(object):

    def __init__(self, event):
        self.tp = 'button_press'
        self.num = event.num
        self.x = event.x
        self.y = event.y

    def __str__(self):
        return '%d:%dx%d' % (self.num, self.x, self.y)

    def __repr__(self):
        return '<%s num=%d x=%d y=%d>' % (self.tp, self.num, self.x, self.y)


class Events(object):

    '''
    keyboard and mouse event processor and state keeper
    '''

    __queue_bound = 1 - 1024

    def __init__(self):
        self.__lock = threading.Lock()
        self.__cond = threading.Condition(self.__lock)
        self.__queue = []
        self.__keys = {}
        self.__pointer_on = False
        self.__pointer_x = 0
        self.__pointer_y = 0
        self.__buttons = {}

    def on_key_press(self, event):
        with self.__cond:
            self.__queue = self.__queue[self.__queue_bound:]
            self.__queue.append(KeyPress(event))
            self.__keys[event.keycode] = event.keysym
            self.__cond.notify()

    def on_key_release(self, event):
        with self.__lock:
            try:
                del self.__keys[event.keycode]
            except KeyError:
                pass

    def on_leave(self, event):
        with self.__lock:
            self.__pointer_on = False
            self.__keys.clear()
            self.__buttons.clear()

    def on_enter(self, event):
        with self.__lock:
            self.__pointer_on = True

    def on_motion(self, event):
        with self.__lock:
            self.__pointer_x = event.x
            self.__pointer_y = event.y

    def on_button_press(self, event):
        with self.__cond:
            self.__queue = self.__queue[self.__queue_bound:]
            self.__queue.append(ButtonPress(event))
            self.__buttons[event.num] = True
            self.__cond.notify()

    def on_button_release(self, event):
        with self.__lock:
            try:
                del self.__buttons[event.num]
            except KeyError:
                pass

    @property
    def keys(self):
        with self.__lock:
            return self.__keys.copy()

    def __event(self, nowait=False):
        with self.__cond:
            if len(self.__queue) == 0:
                if nowait:
                    return None
                self.__cond.wait()
            e = self.__queue.pop(0)
        return e

    @property
    def event(self):
        return self.__event()

    @property
    def event_nowait(self):
        return self.__event(True)

    def event_clear(self):
        with self.__lock:
            self.__queue.clear()

    @property
    def pointer_position(self):
        with self.__lock:
            if self.__pointer_on:
                return (self.__pointer_x, self.__pointer_y)
            return None

    @property
    def buttons(self):
        with self.__lock:
            return self.__buttons.copy()
