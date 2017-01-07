#!/usr/bin/python3
# coding: U8


import types
import inspect

import playwindow


class Para(object):
    prefix = ''
    def __init__(self, text):
        self.text = text
    def __str__(self):
        return self.prefix + self.text

class T1(Para):
    prefix = '# '

class T2(Para):
    prefix = '## '

class T3(Para):
    prefix = '### '

class T4(Para):
    prefix = '#### '


def summary():
    classes = []
    modules = {}
    for name in dir(playwindow):
        if name.startswith('__'):
            continue
        o = getattr(playwindow, name)
        if type(o) is types.ModuleType:
            continue
        if type(o) is type:
            classes.append(T3(name))
            classes.append(Para('Properties: ' + ', '.join('`%s`' % f for f in o._fields)))
            continue
        if type(o) is types.FunctionType:
            mod_name = inspect.getmodule(o).__name__
            if mod_name not in modules:
                modules[mod_name] = []
            modules[mod_name].extend((
                T4('`%s`' % name),
                Para('`%s%s`' % (name, inspect.formatargspec(*inspect.getfullargspec(o))))
                # inspect.cleandoc(inspect.getdoc(o) or '')
            ))
            continue
    return (
        [T1('Summary')] +
        [T2('Funtions')] +
        sum(([T3(m)] + ff for m, ff in modules.items()), []) +
        [T2('Classes')] +
        classes
    )


def main():
    print('\n\n'.join(map(str, summary())))


if __name__ == '__main__':
    main()
