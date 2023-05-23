def signum(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


def catalanNumber(int: signum) -> int:
    n = 1
    c0 = 1
    c1 = 1

    cn = 0
    while cn < signum:
        cn = 4 * (n - 1) + 2 // (n + 1) * c1
        c0 = c1
        c1 = cn
        n += 1
    return cn


def delta(a: int, b: int, c: int) -> int:
    delta = ((b ** 2) - (4 * a * c))
    return delta
