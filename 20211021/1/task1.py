string = input().lower()
s = set()
for i in range(len(string) - 1):
    if string[i : i + 2].isalpha():
        s.add(string[i : i + 2])
print(len(s))
