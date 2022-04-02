"""Utility functions for Dungeon game."""
import shlex

from Dungeon.logic.Monster import Monster


def is_pos_valid(pos):
    """Check if pos is valid or not."""
    return 0 <= pos[0] <= 9 and 0 <= pos[1] <= 9


def move(from_cell, direction):
    """Move main character."""
    moves = {'up': (0, -1), 'down': (0, 1), 'left': (-1, 0), 'right': (1, 0)}
    return (from_cell[0] + moves[direction][0], from_cell[1] + moves[direction][1])


def add_to_map(dungeon_map, args):
    """Add new monster to map."""
    _, _, name, _, hp, _, x, y = shlex.split(args)
    dungeon_map[int(x)][int(y)].append(Monster(name, int(hp)))
    return dungeon_map


def get_present_monsters(dungeon_map):
    """Get list of monsters that are present."""
    monsters = []
    for x, line in zip(range(10), dungeon_map):
        for y, cell in zip(range(10), line):
            for monster in cell:
                monsters.append('{} at ({} {}) hp {}'.format(monster.name, x, y, monster.hp))
    return monsters


def get_completion_attack(dungeon_map, player_pos, prefix):
    """Get words to allow autocompletion."""
    x, y = player_pos
    monster_names = [monster.name for monster in dungeon_map[x][y]]
    return [monster_name for monster_name in monster_names if monster_name.startswith(prefix)]


def get_completion_move(prefix):
    """Get words to allow autocompletion."""
    return [direction for direction in ['up', 'down', 'left', 'right'] if direction.startswith(prefix)]
