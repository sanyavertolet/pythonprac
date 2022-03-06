import textdistance


def dist(s1, s2):
    return textdistance.levenshtein(s1, s2)


def get_valid_string():
    string = ' '
    while ' ' in string:
        string = input()
    return string

