import cmd
import shlex


class Dungeon(cmd.Cmd):
    prompt = '(Dungeon) '
    def do_add(self, args):
        pass


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
