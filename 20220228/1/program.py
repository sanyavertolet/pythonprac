import textdistance

def dist(s1, s2):
    return textdistance.levenshtein(s1, s2)

print(dist(input(), input()))
