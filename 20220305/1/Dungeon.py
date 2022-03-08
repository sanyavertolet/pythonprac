import cmd
import shlex

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def __str__(self):
        return '{} {} hp'.format(self.name, self.hp)

class Dungeon(cmd.Cmd):
    prompt = '(Dungeon) '
    dungeon_map = [[[] for i in range(10)] for i in range(10)]
    player_pos = (0, 0)

    def do_add(self, args):
        _, _, name, _, hp, _, x, y = shlex.split(args)
        self.dungeon_map[int(x)][int(y)].append(Monster(name, int(hp)))

    def do_show(self, args):
        for x, line in zip(range(10), self.dungeon_map):
            for y, cell in zip(range(10), line):
                for monster in cell:
                    print('{} at ({} {}) hp {}'.format(monster.name, x, y, monster.hp))


    def do_attack(self, args):
        monster_name = shlex.split(args)[0]
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


    def is_pos_valid(self, pos):
        return 0 <= pos[0] <= 9 and 0 <= pos[1] <= 9


    def move(self, from_cell, direction):
        moves = {'up': (0, 1), 'down': (0, -1), 'left': (-1, 0), 'right': (1, 0)}
        return (from_cell[0] + moves[direction][0], from_cell[1] + moves[direction][1])

    def do_move(self, args):
        direction = shlex.split(args)[0]
        future_pos = self.move(self.player_pos, direction)
        if self.is_pos_valid(future_pos):
            self.player_pos = future_pos
            x, y = self.player_pos
            print('player at {} {}'.format(x, y))
            if self.dungeon_map[x][y]:
                print('encountered: ' + ', '.join(map(str, self.dungeon_map[x][y])))
        else:
            print('cannot move')


    def complete_attack(self, prefix, line, start_index, end_index):
        pass


    def complete_move(self, prefix, line, start_index, end_index):
        pass

Dungeon().cmdloop()
