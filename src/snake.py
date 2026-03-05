import curses
import random

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # Window setup
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Initial Snake Position
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # Initial Food Position
    food = [sh // 2, sw // 2]
    w.addch(food[0], food[1], '*')

    # Initial Direction
    key = curses.KEY_RIGHT
    
    score = 0

    while True:
        next_key = w.getch()
        
        # If key pressed is valid direction or Quit, update key
        if next_key in [
            curses.KEY_DOWN, curses.KEY_UP, curses.KEY_LEFT, curses.KEY_RIGHT,
            ord('s'), ord('w'), ord('a'), ord('d'),
            ord('q')
        ]:
            key = next_key

        if key == ord('q'):
            break

        # Calculate new head position
        new_head = [snake[0][0], snake[0][1]]

        if key in [curses.KEY_DOWN, ord('s')]:
            new_head[0] += 1
        elif key in [curses.KEY_UP, ord('w')]:
            new_head[0] -= 1
        elif key in [curses.KEY_LEFT, ord('a')]:
            new_head[1] -= 1
        elif key in [curses.KEY_RIGHT, ord('d')]:
            new_head[1] += 1

        # Check Collisions (Walls & Self)
        if (new_head[0] in [0, sh]) or (new_head[1] in [0, sw]) or \
           (new_head in snake):
            break

        # Move Snake
        snake.insert(0, new_head)

        # Check Food
        if snake[0] == food:
            score += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake else None
            w.addch(food[0], food[1], '*')
        else:
            # Move tail
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Draw Head
        try:
            w.addch(snake[0][0], snake[0][1], '#')
        except curses.error:
            pass
            
        # Draw Score
        w.addstr(0, 2, f'Score: {score}')

    curses.endwin()
    print(f"Game Over! Final Score: {score}")

if __name__ == "__main__":
    curses.wrapper(main)
