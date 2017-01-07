#!/usr/bin/python3
# coding: U8


from playwindow import window, oval, wait_for_click, overlapping, from_hsl, raise_item


def main():
    window(300, 200, background='#000')
    oval(20, 20, 180, 180, fill=from_hsl(h=0, s=100, l=100))
    oval(120, 20, 280, 180, fill=from_hsl(h=120, s=100, l=100))
    while True:
        e = wait_for_click()
        oo = overlapping(e.x-1, e.y-1, e.x+1, e.y+1)
        if len(oo) > 0:
            raise_item(oo[-1])


if __name__ == '__main__':
    main()
