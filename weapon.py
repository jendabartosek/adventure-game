from position import Pos
from gui import GUI


class Weapon:

    def __init__(self, name: str, power: int, endurance: int, pos: Pos | None):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.pos = pos
        self.equipped = pos is None

    def equip(self):
        self.equipped = True
        self.pos = None

    def destroy(self):
        self.equipped = False
        self.pos = None

    @property
    def power(self):
        return self.__power

    @property
    def endurance(self):
        return self.__endurance

    @power.setter
    def power(self, value):
        self.__power = value

    @endurance.setter
    def endurance(self, value):
        self.__endurance = value

    def draw(self, gui: GUI):
        if self.equipped:
            return

        gui.set(self.pos.x, self.pos.y, "/")

    def __str__(self):
        return f"{self.name} (P: {self.power}, E: {self.endurance})"
