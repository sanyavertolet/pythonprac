l = list(eval(input()))

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if (l[i] ** 2) % 100 > (l[j] ** 2) % 100:
            l[i], l[j] = l[j], l[i]
print(l)
