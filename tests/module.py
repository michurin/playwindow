# coding: U8


'''
Helper for test_util
'''


from playwindow.util import public


@public
def x(a):
    return a

@public
class X(object): # pylint: disable=too-few-public-methods
    def __init__(self, a):
        self.a = a
    def get_x(self):
        return self.a

def y(): # not public
    pass
