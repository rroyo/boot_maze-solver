from graphics import Window
from maze import Maze
from config import *


def main():
    num_rows = NUM_ROWS
    num_cols = NUM_COLS
    margin = MARGIN
    screen_x = SCREEN_X
    screen_y = SCREEN_Y
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y, BACKGROUND)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    print("Maze created")
    is_solvave = maze.solve(5, 8)
    print("Maze solved!") if is_solvave else print("Maze can't be solved!")

    win.wait_for_close()


main()
