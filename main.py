import random
from gui import GUI
from level import Level
from character import Character
from position import Pos
from typing import List, Tuple
from weapon import Weapon


def run_possible_battles(characters: List[Character]):
    battle_participants = []
    for i, char1 in enumerate(characters):
        for j, char2 in enumerate(characters):
            if i != j and char1.current_pos == char2.current_pos:
                battle_participants.append((char1, char2))

    run_battles(battle_participants)


def equip_possible_weapons(characters: List[Character], weapons: List[Weapon]):
    possible_equipments = []

    for weapon in weapons:
        if weapon.equipped:
            continue

        for char in characters:
            if char.current_pos == weapon.pos:
                possible_equipments.append((char, weapon))

    for equipment in possible_equipments:
        equipment[0].equip_weapon(equipment[1])


def run_battles(battle_possibilities: List[Tuple[Character, Character]]):
    for participants in battle_possibilities:
        currently_attacking_index = random.randint(0, 1)

        while participants[0].is_alive() and participants[1].is_alive() > 0:
            attacker: Character = participants[currently_attacking_index]
            defender: Character = participants[1 - currently_attacking_index]
            damage = defender.defend(attacker.get_attack_power())

            if defender.is_alive():
                print(f"{attacker} attacks at {defender} and gives {damage} damage")
            else:
                print(f"{attacker} was stronger and {defender} died")

            currently_attacking_index = 1 - currently_attacking_index


def draw_game(gui: GUI, level: Level, characters=None, weapons=None):
    if weapons is None:
        weapons = []

    if characters is None:
        characters = []

    level.draw(gui)
    for char in characters:
        char.draw(gui)

    for weapon in weapons:
        weapon.draw(gui)

    gui.draw()


def run_game():
    rows, cols = 10, 10
    level = Level(rows, cols, gate=Pos(7, 7))
    gui = GUI(rows, cols)
    player = Character(level,
                       Pos(1, 1),
                       "Player",
                       12,
                       5,
                       30,
                       player=True)

    enemy = Character(level,
                      Pos(3, 3),
                      "Enemy",
                      8,
                      10,
                      35)

    sword = Weapon("sword", 5, 1, Pos(1, 6))

    all_chars = [player, enemy]
    all_weapons = [sword]

    gui.clear()
    should_draw = True
    while True:
        if should_draw:
            draw_game(gui, level, all_chars, all_weapons)

        direction_to_go = gui.input_direction()

        if direction_to_go is None:
            should_draw = False
            continue

        if player.go(direction_to_go):
            should_draw = True

        if player.is_at_gate():
            if all(not char.is_alive() for char in all_chars if not char.player):
                print("Game finished!")
                break
            else:
                print("Not all enemies dead!")

        run_possible_battles(all_chars)

        if not player.is_alive():
            print("Game over!")
            break

        equip_possible_weapons(all_chars, all_weapons)

    all_chars.clear()
    all_weapons.clear()
    draw_game(gui, level)


if __name__ == '__main__':
    run_game()
