import random
import curses

# Initialize the screen
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()  # Get the screen height and width
w = curses.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)  # Set the screen refresh rate

# Initial snake position and game settings
snake_x = sw // 4
snake_y = sh // 2
snake = [
    [snake_y, snake_x],
    [snake_y, snake_x - 1],
    [snake_y, snake_x - 2]
]

# Initial food position
food = [sh // 2, sw // 2]
w.addch(food[0], food[1], curses.ACS_PI)

# Initial direction (right)
key = curses.KEY_RIGHT

# Main game loop
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # Check if the snake hits the boundary or itself
    if (
        snake[0][0] in [0, sh] or
        snake[0][1] in [0, sw] or
        snake[0] in snake[1:]
    ):
        curses.endwin()
        quit()

    # Calculate the next snake head position based on current direction
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Add the new head to the snake
    snake.insert(0, new_head)

    # If the snake eats food, generate new food and do not remove the last snake element
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh - 1),
                random.randint(1, sw - 1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Move the snake forward, remove the last element
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    # Add the new head to the screen
    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

