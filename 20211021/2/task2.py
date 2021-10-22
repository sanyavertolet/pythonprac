import math

f = dict()

command = input()
while command.split()[0] != 'quit':
    lexems = command.split()
    if len(lexems) == 3:
        f[lexems[0][1:]] = (lexems[1], lexems[2])
    else:
        print(eval(f[lexems[0]][1], math.__dict__, { f[lexems[0]][0]: eval(lexems[1]) }))
    command = input()
print(len(f) + 1)
