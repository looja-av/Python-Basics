import random
import curses

stdscr= curses.initscr()
curses.curs_set(0)
sh, sw= stdscr.getmaxyx()
w= curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)

snake_x= sw // 4
snake_y=sh // 2
snake=[
    [snake_y,snake_x],
    [snake_y,snake_x- 1],
    [snake_y,snake_x- 2]
]

food= [sh//2, sw//2]
w.addch(food[0],food[1],curses.ACS_PI)

key= curses.KEY_RIGHT

while True:
    next_key=w.getch()
    key in key if next_key==-1 else next_key

    if(
        snake[0][0] in[0,sh] or
        snake[0][1] in[0,sw] or
        snake[0] in snake[1:] 
    ):
        curses.endwin()
        quit()



