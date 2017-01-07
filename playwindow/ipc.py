# coding: U8


import logging
import os
import re
import time
import itertools
import subprocess
import tkinter


logger = logging.getLogger(__name__)


special_chars_replacement_re = re.compile(r'[\\$"{}[]')


def tk_escape(v):
    if isinstance(v, str):
        if v == '':
            return '{}'
        return '"' + special_chars_replacement_re.sub(
            lambda m: '\\' + m.group(0),
            v
        ) + '"'
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, (list, tuple)):
        return '{' + ' '.join(tk_struct_array(v)) + '}'
    if isinstance(v, dict):
        return '{' + ' '.join(tk_struct_dict(v)) + '}'
    raise TypeError('Unsupprted type %r: %r' % (type(v), v))


def tk_struct_array(v):
    for x in v:
        yield tk_escape(x)


def tk_struct_dict(v):
    for k, x in v.items():
        if x is not None:
            yield '-' + str(k)
            yield tk_escape(x)


class Window(object): # pylint: disable=too-few-public-methods

    def __init__(self, appname):
        self.appname = appname
        self.tk_window = None
        self.debug_mode = False

    def __raise_client(self):
        self.tk_window = tkinter.Tk()
        self.tk_window.withdraw()

    def __ping(self):
        try:
            self.tk_window.send(self.appname, 'ping')
        except tkinter.TclError as exc:
            arg0 = exc.args[0]
            if (
                    arg0.startswith('target application died') or
                    arg0.startswith('no application named')
                ):
                return False
            raise
        return True

    def __raise_server(self):
        if self.__ping():
            logger.debug('drop existed window')
            self.tk_window.send(self.appname, 'stop')
        delay = 0.05
        script_path = os.path.join(os.path.dirname(__file__), 'gui/playwindow.tcl')
        while delay < 4:
            logger.debug('try to start server; delay=%r', delay)
            if self.__ping():
                break
            env_copy = os.environ.copy()
            if self.debug_mode:
                env_copy['playwindow_debug'] = '1'
            subprocess.Popen(
                (
                    script_path,
                    script_path
                ),
                shell=False,
                stdin=None,
                stdout=None,
                stderr=None,
                close_fds=True,
                preexec_fn=os.setpgrp, # don't forward signals
                env=env_copy
            )
            time.sleep(delay)
            delay *= 2
        else:
            raise RuntimeError('Can not run server')

    def __call__(self, *args, **kvargs):
        it_is_first_call = self.tk_window is None
        if it_is_first_call:
            self.__raise_client()
            self.__raise_server()
        tk_args = tuple(itertools.chain(tk_struct_array(args), tk_struct_dict(kvargs)))
        logger.debug('tk_args: %r', tk_args)
        result = self.tk_window.send(self.appname, *tk_args)
        return result

    def debug(self, debug):
        self.debug_mode = bool(debug)


tk_call = Window('playwindow')
