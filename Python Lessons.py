# Задание 1


def step(a, b):
    if b == 1:
        return a
    else:
        return a * step(a, b-1)


print(step(5, 6))


# Задание 2

def sum_41(a, b):
    if b == 0:
        return a
    return sum_41(a+1, b-1)


print(sum_41(4, 10))
