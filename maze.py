from cell import Cell
import random
import time
from config import *


class Maze:
    def __init__(
        self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None
    ):
        self._cells = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(DRAW_SPEED)

    def _break_walls_r(self, i, j):
        current = self._cells[i][j]
        current.visited = True

        while True:
            to_visit = []

            # checking cells directly adjacent to current

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # right
            if i + 1 < self._num_cols and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # top
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # bottom
            if j + 1 < self._num_rows and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            # zero directions to go, break loop
            if not to_visit:
                # current.draw(current._x1, current._y1, current._x2, current._y2)
                self._draw_cell(i, j)
                return

            # pick a random adjacent cell
            next_cell = to_visit[random.randrange(len(to_visit))]

            # break common walls
            # next cell is left cell
            if next_cell[0] == i - 1:
                current.has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # next cell is right cell
            if next_cell[0] == i + 1:
                current.has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # next cell is top cell
            if next_cell[1] == j - 1:
                current.has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            # next cell is bottom cell
            if next_cell[1] == j + 1:
                current.has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False

            # move to the choosen adjacent cell
            self._break_walls_r(next_cell[0], next_cell[1])

    def _break_entrance_and_exit(self):
        start = self._cells[0][0]
        start.has_top_wall = False
        self._draw_cell(0, 0)

        end = self._cells[self._num_cols - 1][self._num_rows - 1]
        end.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def solve(self, i=0, j=0):
        return self._solve_r(i, j)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # is it the end cell?
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # look in each direction
        # left
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not current_cell.has_left_wall
        ):
            current_cell.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            current_cell.draw_move(self._cells[i - 1][j], True)

        # right
        if (
            i + 1 < self._num_cols
            and not self._cells[i + 1][j].visited
            and not current_cell.has_right_wall
        ):
            current_cell.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            current_cell.draw_move(self._cells[i + 1][j], True)
        # top
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not current_cell.has_top_wall
        ):
            current_cell.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            current_cell.draw_move(self._cells[i][j - 1], True)
        # bottom
        if (
            j + 1 < self._num_rows
            and not self._cells[i][j + 1].visited
            and not current_cell.has_bottom_wall
        ):
            current_cell.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            current_cell.draw_move(self._cells[i][j + 1], True)

        # No direction worked out
        return False
