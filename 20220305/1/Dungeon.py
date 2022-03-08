import cmd
import shlex

class Monster:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
    def __str__():
        pass 

class Dungeon(cmd.Cmd):
    prompt = '(Dungeon) '
    dungeon_map = [[[] for i in range(10)] for i in range(10)]
    

    def do_add(self, args):
        _, _, name, _, hp, _, x, y = shlex.split(args)
        self.dungeon_map[x][y].append(Monster(name, int(hp))
        


    def do_show(self, args):
        pass


    def do_attack(self, args):
        pass


    def do_move(self, args):
        pass


    def complete_attack(self, prefix, line, start_index, end_index):
        pass


    def complete_move(self, prefix, line, start_index, end_index):
        pass

Dungeon().cmdloop()
