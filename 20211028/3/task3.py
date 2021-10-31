print(' '.join(list(filter(lambda word: word.count('TOR') == 2, [''.join(product) for product in __import__('itertools').product('TOR', repeat=int(input()))]))))
