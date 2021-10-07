def Pareto(*pairs):
    result = []
    for pair_1 in pairs:
        for pair_2 in pairs:
            if pair_1[0] <= pair_2[0] and pair_1[1] <= pair_2[1] and (pair_1[0] < pair_2[0] or pair_1[1] < pair_2[1]):
                break
        else:
            result.append(pair_1)
    return tuple(result)

print(Pareto(*eval(input())))
