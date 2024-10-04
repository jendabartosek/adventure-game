from gui import GUI
from position import Pos
import utils


class Level:

    def __init__(self, rows: int, cols: int, gate: Pos):
        self.cols = cols
        self.rows = rows
        self.map = [' '] * (cols * rows)
        self.gate = gate
        self._set_borders()

    def is_open_space(self, pos: Pos) -> bool:
        x = pos.x
        y = pos.y
        if x < 0 or x >= self.cols or y < 0 or y >= self.rows:
            return False

        area = self.map[self._get_index(x, y)]
        return area != "#"

    def draw(self, gui: GUI):
        for x in range(self.rows):
            for y in range(self.cols):
                gui.set(x, y, self.map[self._get_index(x, y)])

        gui.set(self.gate.x, self.gate.y, "^")

    def _set_borders(self):
        for x in range(self.rows):
            for y in range(self.cols):
                if x == 0 or x == self.rows - 1 or y == 0 or y == self.cols - 1:
                    index = self._get_index(x, y)
                    self.map[index] = '#'

    def _get_index(self, x, y) -> int:
        return utils.flattened_index(x, y, self.cols)
