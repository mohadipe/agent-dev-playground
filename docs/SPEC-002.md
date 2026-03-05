# SPEC-002: Snake Game in Terminal

## 1. Goal
Implement a classic Snake game that runs in the terminal using Python.

## 2. Architecture
*   **File:** `src/snake.py`
*   **Repo:** `agent-dev-playground`

## 3. Requirements
*   **Language:** Python 3
*   **Libraries:** `curses` (Standard Library) - for terminal graphics and input handling.
*   **Controls:** WASD (Up/Left/Down/Right), Q to quit.

## 4. Implementation Details
*   **Game Loop:** Use `curses.wrapper` to initialize. A `while` loop handles the game state.
*   **State:** 
    *   `snake`: List of coordinates `[(y, x), ...]`.
    *   `food`: Coordinate `(y, x)`.
    *   `score`: Integer.
*   **Logic:**
    *   Update snake head position based on direction.
    *   Check collision with walls -> Game Over.
    *   Check collision with self -> Game Over.
    *   Check collision with food -> Grow snake, spawn new food, increase score.
*   **Rendering:**
    *   Clear screen.
    *   Draw border.
    *   Draw snake (`#` or `O`).
    *   Draw food (`*`).
    *   Draw score.
