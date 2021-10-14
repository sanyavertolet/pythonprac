from fractions import Fraction

def polynom(x, power, a) -> Fraction:
    result = Fraction(a[0])
    for i in range(1, power + 1):
        result *= x
        result += Fraction(a[i])
    return result

def process(s, w, power_a, c_a, power_b, c_b):
    if polynom(s, power_b, c_b) == 0:
        return False
    return (polynom(s, power_a, c_a) / polynom(s, power_b, c_b) == w)

def get_input():
    input_list = input().split(',')
    input_list = [s.strip() for s in input_list]
    s, w = Fraction(input_list[0]), Fraction(input_list[1])
    power_a = int(input_list[2])
    c_a = input_list[3:4 + power_a]
    power_b = int(input_list[4 + power_a])
    c_b = input_list[5 + power_a:]
    return s, w, power_a, c_a, power_b, c_b

s, w, power_a, c_a, power_b, c_b = get_input()
print(process(s, w, power_a, c_a, power_b, c_b))
