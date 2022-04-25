"""CLI interaction implementation."""
import cmd
import shlex

from ..logic import DungeonUtils as utils


class Dungeon(cmd.Cmd):
    """Class that implements game."""
    prompt = '(Dungeon) '
    dungeon_map = [[[] for i in range(10)] for i in range(10)]
    player_pos = (0, 0)

    def do_add(self, args):
        """Add new monster.
        
        :param args: command line arguments
        :type args: list[str]
        :return: None
        :rtype: None
        """
        self.dungeon_map = utils.add_to_map(self.dungeon_map, args)

    def do_show(self, args):
        """Print monsters from certain cell.

        :param args: command line arguments
        :type args: list[str]
        :return: None
        :rtype: None
        """
        monsters = utils.get_present_monsters(self.dungeon_map)
        for monster in monsters:
            print(monster)

    def do_attack(self, args):
        """Attack monster.

        :param args: command line arguments
        :type args: list[str]
        :return: None
        :rtype: None
        """
        monster_name = args
        x, y = self.player_pos
        monsters = self.dungeon_map[x][y]
        for monster in monsters:
            if monster.name == monster_name:
                monster.hp -= 10
                if monster.hp > 0:
                    print('{} lost 10 hp, now has {} hp'.format(monster.name, monster.hp))
                else:
                    print('{} dies'.format(monster.name))
                    monsters.remove(monster)
                break
        else:
            print('no {} here'.format(monster_name))

    def do_move(self, args):
        """Move main character.

        :param args: command line arguments
        :type args: list[str]
        :return: None
        :rtype: None
        """
        direction = shlex.split(args)[0]
        future_pos = utils.move(self.player_pos, direction)
        if utils.is_pos_valid(future_pos):
            self.player_pos = future_pos
            x, y = self.player_pos
            print('player at {} {}'.format(x, y))
            if self.dungeon_map[x][y]:
                print('encountered: ' + ', '.join(map(str, self.dungeon_map[x][y])))
        else:
            print('cannot move')

    def complete_attack(self, prefix, line, start_index, end_index):
        """Autocomplete attack command.

        :param prefix: command prefix
        :param line: unused
        :param start_index: unused
        :paramend_index: unused
        :type prefix: str
        :type line: str
        :type start_index: int
        :type end_index: int
        :return: list of autocompletions needed by cmd module
        :rtype: list[str]
        """
        return utils.get_completion_attack(self.dungeon_map, self.player_pos, prefix)

    def complete_move(self, prefix, line, start_index, end_index):
        """Autocomplete move command.

        :param prefix: command prefix
        :param line: unused
        :param start_index: unused
        :paramend_index: unused
        :type prefix: str
        :type line: str
        :type start_index: int
        :type end_index: int
        :return: list of autocompletions needed by cmd module
        :rtype: list[str]
        """
        return utils.get_completion_move(prefix)
