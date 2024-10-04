class Pos:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @x.setter
    def x(self, value):
        self.__x = value

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
