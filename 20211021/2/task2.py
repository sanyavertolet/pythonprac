import math

f = dict() # f[fname] = (var1, var2, ..., expr)

counter = 1
command = input()
while command.split()[0] != 'quit':
    counter += 1
    lexems = command.split()
    if lexems[0][0] == ':':
        f[lexems[0][1:]] = lexems[1:]
    else:
        fname = lexems[0]
        val = lexems[1:]
        var = f[fname][:len(f[fname]) - 1]
        expr = f[fname][-1]
        var_dict = { vr: eval(vl) for vr, vl in zip(var, val)}
        print(eval(expr, math.__dict__, var_dict))
    command = input()
print(command.split()[1].format(len(f) + 1, counter))
