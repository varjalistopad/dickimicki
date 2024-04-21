import curses
import time
from math import cos, radians

def draw_dick(win, angle):
    dick = [
        '                        &@@@ @@@#',
        '                      @@@@@@ @@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                     @@@@@@@@@@@@@@@',
        '                  *(*@@@@@@@@@@@@@@@*(*',
        '            /@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.',
        '           &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#',
        '          @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
        '           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
        '            #@@@@@@@@@@@@@@@   @@@@@@@@@@@@@*',
        '              /@@@@@@@@@         @@@@@@@@/',
    ]
    h = len(dick)
    w = max(len(line) for line in dick)
    cx, cy = w // 2, h // 2
    # Увеличиваем offset_y на 4 строки
    offset_x, offset_y = (curses.COLS - w) // 2, (curses.LINES - h) // 10 + 8

    for y in range(h):
        for x in range(w):
            if x < len(dick[y]):
                char = dick[y][x]
            else:
                char = ' '
            if char != ' ':
                dx = x - cx
                nx = int(cx + dx * cos(angle)) + offset_x
                ny = y + offset_y  # сохраняем y без изменений
                if 0 <= nx < curses.COLS and 0 <= ny < curses.LINES:
                    try:
                        win.addch(ny, nx, char)
                    except curses.error:
                        pass  # ignore all errors gracefully

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    angle = 0
    while True:
        stdscr.clear()
        draw_dick(stdscr, radians(angle))
        stdscr.refresh()
        time.sleep(0.05)
        angle = (angle + 2) % 360  # угол изменяется для поворота по оси X
        if stdscr.getch() == ord('q'):
            break

curses.wrapper(main)
