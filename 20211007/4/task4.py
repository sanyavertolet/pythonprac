from math import *

#f(g_1(x), g_2(x))

def Calc(s, t, u):
    g_1 = lambda x: eval(s)
    g_2 = lambda x: eval(t)
    def f(v):
        x = g_1(v)
        y = g_2(v)
        return eval(u)
    return f

print(Calc(*eval(input()))(eval(input())))
