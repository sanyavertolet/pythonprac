from collections import defaultdict
w = int(input())

freq = defaultdict(int)

string = input()
while string != '':
    new_string = []
    for ch in string:
        if ch.isalpha():
            new_string.append(ch.lower())
        else:
            new_string.append(' ')
    string = ''.join(new_string)
    for word in string.split():
        if len(word) == w:
            freq[word] += 1
    string = input()

result = []
if len(freq) != 0:
    max_freq = max(freq.values())
    for item in freq.items():
        if item[1] == max_freq:
            result.append(item[0])
    print(' '.join(sorted(result)))
