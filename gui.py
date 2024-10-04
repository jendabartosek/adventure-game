from direction import Direction
import utils
import keyboard


class GUI:

    def __init__(self, rows: int, cols: int):
        self.cols = cols
        self.rows = rows
        self.canvas = [' '] * (cols * rows)

    def clear(self):
        for i in range(len(self.canvas)):
            self.canvas[i] = ' '

    def set(self, x: int, y: int, char: str):
        if len(char) != 1:
            raise ValueError("Input must be a single character.")

        index = utils.flattened_index(x, y, self.cols)

        if index < 0 or index > len(self.canvas):
            raise ValueError("Position (x, y) is out of bounds.")

        self.canvas[index] = char

    def draw(self):
        print()
        for i in range(self.rows):
            start = i * self.cols
            end = start + self.cols
            row = self.canvas[start:end]
            for char in row:
                print(char, end=" ")
            print()
        print()

    @staticmethod
    def input_direction():

        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'up':
                return Direction.NORTH
            elif event.name == 'down':
                return Direction.SOUTH
            elif event.name == 'left':
                return Direction.WEST
            elif event.name == 'right':
                return Direction.EAST
            else:
                return None
