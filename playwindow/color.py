# coding: U8


from playwindow.util import public


@public
def from_rgb(r, g, b):
    '''
    r 0-100 (red)
    g 0-100 (green)
    b 0-100 (blue)
    '''
    return '#' + ''.join('%02x' % min(max(int(x * 2.55 + 0.5), 0), 255) for x in (r, g, b))


@public
def from_cmy(c, m, y):
    '''
    c 0-100 (cyan)
    m 0-100 (magenta)
    y 0-100 (yellow)
    '''
    return from_rgb(
        100. - c,
        100. - m,
        100. - y
    )


@public
def from_hsl(h, s, l):
    '''
    h 0-360 (hue)
    s 0-100 (saturation)
    l 0-100 (light)
    '''
    lmin = (100. - s) * l / 100.
    a = (l - lmin) * (h % 60) / 60.
    linc = lmin + a
    ldec = l - a
    m = (
        (0, 1, 3),
        (2, 0, 3),
        (3, 0, 1),
        (3, 2, 0),
        (1, 3, 0),
        (0, 3, 2),
    )[int((h % 360) / 60.)]
    r, g, b = [(l, linc, ldec, lmin)[k] for k in m]
    return from_rgb(r, g, b)
