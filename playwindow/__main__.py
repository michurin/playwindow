# coding: utf-8


def scope():
    import sys, os, readline, errno, atexit, rlcompleter
    sys.ps1 = '\001\033[32;1m\002>>>\001\033[0m\002 '
    sys.ps2 = '\001\033[32m\002...\001\033[0m\002 '
    histfile = os.path.join(os.environ["HOME"], ".pyhistwin")
    try:
        readline.read_history_file(histfile)
    except IOError as ex:
        if ex.errno != errno.ENOENT:
            pass
    atexit.register(readline.write_history_file, histfile)
    readline.parse_and_bind("tab: complete")
    print('''\001\033[1;33m\002Welcome to playwindow\001\033[0m\002
Try:
-----------------------------
\001\033[32m\002>>>\001\033[0m\002 win.background('#444444')
\001\033[32m\002>>>\001\033[0m\002 w, h = win.size
\001\033[32m\002>>>\001\033[0m\002 win.oval(0, 0, w, h, fill='#005500')
\001\033[32m\002>>>\001\033[0m\002 win.oval(0, 0, w/2, h, fill='#005500', tags='one')
\001\033[32m\002>>>\001\033[0m\002 win.move('one', w/2, 0)
\001\033[32m\002>>>\001\033[0m\002 for x in range(0, int(w/2)): win.move('one', -1, 0); sleep(.02)
\001\033[32m\002...\001\033[0m\002
\001\033[32m\002>>>\001\033[0m\002 win.config('all', width=8, outline='#00ff00')
\001\033[32m\002>>>\001\033[0m\002 win.delete('all')
\001\033[32m\002>>>\001\033[0m\002 demo_all()
-----------------------------
''')


scope()
del scope


from playwindow import win
from playwindow.demo import demo_all
from time import sleep
