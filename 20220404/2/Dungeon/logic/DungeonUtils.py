"""Utility functions for Dungeon game."""
import shlex

from .Monster import Monster


def is_pos_valid(pos):
    """Check if pos is valid or not.

    :param pos: position for the check
    :type pos: tuple[int, int]
    :return: `True` if position is valid, `False` otherwise
    :rtype: bool
    """
    return 0 <= pos[0] <= 9 and 0 <= pos[1] <= 9


def move(from_cell, direction):
    """Move main character.

    :param from_cell: current position
    :param direction: direction of where to go
    :type from_cell: tuple[int, int]
    :type direction: str
    :return: new position
    :rtype: tuple[int]
    """
    moves = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
    return (from_cell[0] + moves[direction][0], from_cell[1] + moves[direction][1])


def add_to_map(dungeon_map, args):
    """Add new monster to map.

    :param dungeon_map: map of a current game
    :param args: info about mosnter to place
    :type dungeon_map: list[list[list[Monster]]]
    :type args: list[str]
    :return: updated dungeon map
    :rtype: list[list[list[Monster]]]
    """
    _, _, name, _, hp, _, x, y = shlex.split(args)
    dungeon_map[int(x)][int(y)].append(Monster(name, int(hp)))
    return dungeon_map


def get_present_monsters(dungeon_map):
    """Get list of monsters that are present.

    :param dungeon_map: map of a current game
    :type dungeon_map: list[list[list[Monster]]]
    :return: list of monster that are present on the map
    :rtype: list[str]
    """
    monsters = []
    for x, line in zip(range(10), dungeon_map):
        for y, cell in zip(range(10), line):
            for monster in cell:
                monsters.append('{} at ({} {}) hp {}'.format(monster.name, x, y, monster.hp))
    return monsters


def get_completion_attack(dungeon_map, player_pos, prefix):
    """Get words to allow autocompletion.

    :param dungeon_map: map of a current game
    :param player_pos: current player's position
    :param prefix: string that is written by this time
    :type dungeon_map: list[list[list[Monster]]]
    :type player_pos: tuple[int]
    :type prefix: str
    :return: list of possible completions
    :rtype: list[str]
    """
    x, y = player_pos
    monster_names = [monster.name for monster in dungeon_map[x][y]]
    return [monster_name for monster_name in monster_names if monster_name.startswith(prefix)]


def get_completion_move(prefix):
    """Get words to allow autocompletion.

    :param prefix: get autocompletion by prefix
    :type prefix: str
    :return: list of possible completions
    :rtype: list[str]
    """
    return [direction for direction in ['up', 'down', 'left', 'right'] if direction.startswith(prefix)]
