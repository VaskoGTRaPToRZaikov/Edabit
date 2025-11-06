import math


def solve_for_exp(a, b):
    x = round(math.log(b) / math.log(a))
    if a ** x == b:
        return x
    return None