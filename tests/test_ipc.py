# coding: U8


import pytest

from playwindow.ipc import tk_call as tk_call_


class FakeWindow(object):

    def __init__(self):
        self.args = None

    def send(self, *args):
        self.args = args


@pytest.fixture
def tk_call():
    tk_call_.tk_window = FakeWindow()
    return tk_call_


@pytest.mark.parametrize('args,kvargs,res', (
    (('x',), {}, ('"x"',)),
    (('',), {}, ('{}',)),
    (('{',), {}, (r'"\{"',)),
    (('\$"{}[',), {}, (r'"\\\$\"\{\}\["',)),
    (('"',), {}, (r'"\""',)),
    ((' ',), {}, (r'" "',)),
    (('\n\t',), {}, ('"\n\t"',)),
    (('[]',), {}, (r'"\[]"',)), # yes, it is correct tcl square brackets escaping
    ((1,), {}, ('1',)),
    ((1.0,), {}, ('1.0',)),
    ((), {'p': 'q'}, ('-p', '"q"')),
    ((), {'p': 1}, ('-p', '1')),
    ((), {'p': 'a', 'q': None}, ('-p', '"a"')),
    ((), {'l': ['a', 'b']}, ('-l', '{"a" "b"}')),
    ((), {'ll': [['a', 'b'], ['p', 'q']]}, ('-ll', '{{"a" "b"} {"p" "q"}}')),
    ((), {'d': {'a': 'b'}}, ('-d', '{-a "b"}')),
))
def test_low_level_call(tk_call, args, kvargs, res):
    tk_call(*args, **kvargs)
    assert tk_call.tk_window.args == (tk_call.appname,) + res
