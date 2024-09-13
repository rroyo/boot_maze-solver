import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def setUp(self):
        self.num_cols = 12
        self.num_rows = 10
        self.maze = Maze(0, 0, self.num_rows, self.num_cols, 10, 10)

    def test_maze_create_cells(self):
        self.assertEqual(len(self.maze._cells), self.num_cols)
        self.assertEqual(len(self.maze._cells[0]), self.num_rows)

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 16
        maze = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(maze._cells), num_cols)
        self.assertEqual(len(maze._cells[0]), num_rows)

    def test_start_end_cells(self):
        start = self.maze._cells[0][0]
        end = self.maze._cells[self.num_cols - 1][self.num_rows - 1]
        self.assertEqual(start.has_top_wall, False)
        self.assertEqual(end.has_bottom_wall, False)

    def test_reset_cells_visited(self):
        for row in self.maze._cells:
            for cell in row:
                self.assertEqual(cell.visited, False)


if __name__ == "__main__":
    unittest.main()
