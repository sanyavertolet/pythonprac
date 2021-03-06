import multiprocessing
import textdistance


def dist(s1, s2, s3):
    if s3 == 'L':
        return textdistance.levenshtein(s1, s2)
    elif s3 == 'D':
        return textdistance.damerau_levenshtein(s1, s2)
    else:
        return -1


def get_valid_string():
    string = ' '
    while ' ' in string:
        string = input()
    return string

s1 = get_valid_string()
s2 = get_valid_string()
s3 = get_valid_string()

with multiprocessing.Pool(1) as pool:
    process = pool.apply_async(dist, (s1, s2, s3))
    try:
        res = process.get(timeout=1)
    except multiprocessing.context.TimeoutError:
        res = -1

print(res)

