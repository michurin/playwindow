#!/usr/bin/python3
# coding: U8


from playwindow import window, window_cursor, text, wait_for_move, overlapping


CURSORS = (
    'X_cursor',
    'arrow',
    'based_arrow_down',
    'based_arrow_up',
    'boat',
    'bogosity',
    'bottom_left_corner',
    'bottom_right_corner',
    'bottom_side',
    'bottom_tee',
    'box_spiral',
    'center_ptr',
    'circle',
    'clock',
    'coffee_mug',
    'cross',
    'cross_reverse',
    'crosshair',
    'diamond_cross',
    'dot',
    'dotbox',
    'double_arrow',
    'draft_large',
    'draft_small',
    'draped_box',
    'exchange',
    'fleur',
    'gobbler',
    'gumby',
    'hand1',
    'hand2',
    'heart',
    'icon',
    'iron_cross',
    'left_ptr',
    'left_side',
    'left_tee',
    'leftbutton',
    'll_angle',
    'lr_angle',
    'man',
    'middlebutton',
    'mouse',
    'none',
    'pencil',
    'pirate',
    'plus',
    'question_arrow',
    'right_ptr',
    'right_side',
    'right_tee',
    'rightbutton',
    'rtl_logo',
    'sailboat',
    'sb_down_arrow',
    'sb_h_double_arrow',
    'sb_left_arrow',
    'sb_right_arrow',
    'sb_up_arrow',
    'sb_v_double_arrow',
    'shuttle',
    'sizing',
    'spider',
    'spraycan',
    'star',
    'target',
    'tcross',
    'top_left_arrow',
    'top_left_corner',
    'top_right_corner',
    'top_side',
    'top_tee',
    'trek',
    'ul_angle',
    'umbrella',
    'ur_angle',
    'watch',
    'xterm',
)


def main():
    window(600, 600, background='#000')
    n = 0
    object_id_to_cursor = dict()
    for y in range(50, 551, 25):
        for x in range(100, 501, 133):
            if n >= len(CURSORS):
                break
            cursor = CURSORS[n]
            o = text(x, y, cursor)
            object_id_to_cursor[o] = cursor
            n += 1
    while True:
        e = wait_for_move()
        oo = overlapping(e.x-1, e.y-1, e.x+1, e.y+1)
        if len(oo) > 0:
            o = oo[-1]
            window_cursor(object_id_to_cursor[o])


if __name__ == '__main__':
    main()
