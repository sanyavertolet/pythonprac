import random


a = [random.randint(1, 100) for i in range(9)]
a.append(int(input()))
random.shuffle(a)
print(a)
