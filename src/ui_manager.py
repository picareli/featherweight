import curses
from curses import wrapper

def main(stdscr):
    stdscr.clear()

    win = curses.newwin(20, 50, 0, 0)
    
    win.addstr("Hello there,")

    win.refresh()

wrapper(main)