def getNumber(number):
    if number%15 == 0:
        return 'BOTH'
    elif number%3 == 0:
        return 'THREE'
    elif number%5 == 0:
        return 'FIVE'
    return number


def getNumberRange(first, last):
    step = 1
    if first > last:
        step = -1
    return [ getNumber(k) for k in range(first, last + step, step)]
