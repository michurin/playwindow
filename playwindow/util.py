# coding: U8


import sys


def public(f):
    a = sys.modules[f.__module__].__dict__.setdefault('__all__', [])
    if f.__name__ not in a:
        a.append(f.__name__)
    return f
