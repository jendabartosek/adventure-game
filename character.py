from level import Level
from direction import Direction
from gui import GUI
from position import Pos
from weapon import Weapon
from hand import Hand
from typing import Dict


class Character:

    def __init__(self,
                 level: Level,
                 start_pos: Pos,
                 name: str,
                 power: int,
                 agility: int,
                 health: int,
                 player: bool = False):
        self.player: bool = player
        self.level: Level = level
        self.current_pos: Pos = start_pos
        self.name: str = name
        self.power: int = power
        self.agility: int = agility
        self.health: int = health
        self.current_health: int = health
        self.equipment: Dict[Hand, Weapon] = {}

    def is_at_gate(self) -> bool:
        return self.current_pos == self.level.gate

    def is_alive(self) -> bool:
        return self.current_health > 0

    def go(self, direction: Direction) -> bool:
        tmp_x = self.current_pos.x
        tmp_y = self.current_pos.y

        if direction == Direction.NORTH:
            tmp_y -= 1
        elif direction == Direction.SOUTH:
            tmp_y += 1
        elif direction == Direction.WEST:
            tmp_x -= 1
        else:
            tmp_x += 1

        next_move = Pos(tmp_x, tmp_y)
        is_allowed = self.level.is_open_space(next_move)

        if is_allowed:
            self.current_pos = Pos(tmp_x, tmp_y)

        return is_allowed

    def equip_weapon(self, weapon: Weapon):
        if Hand.LEFT not in self.equipment or self.equipment[Hand.LEFT] is None:
            print(f"{self} equips {weapon}!")
            self.equipment[Hand.LEFT] = weapon
            weapon.equip()
            return

        if Hand.RIGHT not in self.equipment or self.equipment[Hand.RIGHT] is None:
            print(f"{self} equips {weapon}!")
            self.equipment[Hand.RIGHT] = weapon
            weapon.equip()
            return

        print(f"{str()} has full hands!")

    def defend(self, attack: int) -> int:
        total_endurance = self._get_defense()

        damage = max(0, attack - total_endurance)

        self.current_health -= damage

        return damage

    def _get_defense(self) -> int:
        endurance = self.agility

        if Hand.LEFT in self.equipment:
            weapon = self.equipment.get(Hand.LEFT, None)
            endurance += weapon.endurance if weapon is not None else 0

        if Hand.RIGHT in self.equipment:
            weapon = self.equipment.get(Hand.RIGHT, None)
            endurance += weapon.endurance if weapon is not None else 0

        return endurance

    def get_attack_power(self) -> int:
        attack = self.power

        if Hand.LEFT in self.equipment:
            weapon = self.equipment.get(Hand.LEFT, None)
            attack += weapon.power if weapon is not None else 0

        if Hand.RIGHT in self.equipment:
            weapon = self.equipment.get(Hand.RIGHT, None)
            attack += weapon.power if weapon is not None else 0

        return attack

    def draw(self, gui: GUI):
        if not self.is_alive():
            return

        avatar = "@" if self.player else "O"
        gui.set(self.current_pos.x, self.current_pos.y, avatar)

    def __str__(self):
        return (f"{self.name} [H: {self.current_health}/{self.health}] (P: {self.get_attack_power()},"
                f" A: {self._get_defense()})")
