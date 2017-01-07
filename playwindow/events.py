# coding: U8


import collections
import random
import time

from playwindow.ipc import tk_call
from playwindow.util import public


EventMouseMove = public(collections.namedtuple('EventMouseMove', ('x', 'y')))
EventMouseButtonPress = public(collections.namedtuple('EventMouseButtonPress', ('x', 'y', 'button')))
EventMouseButtonRelease = public(collections.namedtuple('EventMouseButtonRelease', ('x', 'y', 'button')))
EventMouseEnter = public(collections.namedtuple('EventMouseEnter', ('x', 'y')))
EventMouseLeave = public(collections.namedtuple('EventMouseEnter', ('x', 'y')))
EventKeyPress = public(collections.namedtuple('EventKeyPress', ('code', 'state', 'key')))
EventKeyRelease = public(collections.namedtuple('EventKeyRelease', ('code', 'state', 'key')))
EventConfigure = public(collections.namedtuple('EventConfigure', ('width', 'height')))
EventTimer = public(collections.namedtuple('EventTimer', ('name')))


def __typefy(cls, typemap, args):
    return cls(*(tp(a) for tp, a in zip(typemap, args)))


@public
def wait():
    while True:
        event = tk_call('wait').split()
        etype = event[0]
        etail = event[1:]
        if etype == 'internal_tik':
            # special tiks to return to Python scope pereodicaly
            continue
        elif etype == 'mouse_move':
            return __typefy(EventMouseMove, (int, int), etail)
        elif etype == 'mouse_button_press':
            return __typefy(EventMouseButtonPress, (int, int, int), etail)
        elif etype == 'mouse_button_release':
            return __typefy(EventMouseButtonRelease, (int, int, int), etail)
        elif etype == 'mouse_enter':
            return __typefy(EventMouseEnter, (int, int), etail)
        elif etype == 'mouse_leave':
            return __typefy(EventMouseLeave, (int, int), etail)
        elif etype == 'key_press':
            return __typefy(EventKeyPress, (int, int, str), etail)
        elif etype == 'key_release':
            return __typefy(EventKeyRelease, (int, int, str), etail)
        elif etype == 'alert':
            return __typefy(EventTimer, (str,), etail)
        elif etype == 'configure':
            return __typefy(EventConfigure, (int, int), etail)
        else:
            raise NotImplementedError('event = %r' % event)


@public
def schedule(timeout, name=None):
    if name is None:
        name = 'noname'
    return str(tk_call('schedule', int(timeout * 1000), name))


@public
def wait_for_click():
    while True:
        event = wait()
        if type(event) is EventMouseButtonPress: # pylint: disable=unidiomatic-typecheck
            return event


@public
def wait_for_move():
    while True:
        event = wait()
        if type(event) is EventMouseMove: # pylint: disable=unidiomatic-typecheck
            return event


@public
def wait_for_key():
    while True:
        event = wait()
        if type(event) is EventKeyPress: # pylint: disable=unidiomatic-typecheck
            return event


@public
def sleep(timeout):
    name = 'random_name_%04d_%f' % (random.randrange(10000), time.time())
    schedule(timeout, name)
    while True:
        event = wait()
        if type(event) is EventTimer: # pylint: disable=unidiomatic-typecheck
            if event.name == name: # pylint: disable=no-member
                return
