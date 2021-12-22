a, b = eval(input())
print([x for x in range(a if a != 1 else a + 1, b) if all([x % j != 0 for j in range(2, x)])])
